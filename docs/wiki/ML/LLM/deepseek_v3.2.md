---
layout: page
title: DeepSeek V3.2
author: Yifei Zhu
comments: true
tags:
  - ML
  - AI
  - LLM
---
# 2025.12.01 DeepSeek V3.2 发布

DeepSeek V3.2 正式版：强化 Agent 能力，融入思考推理

DeepSeek 3.2 实现了一个行业突破：**在推理过程中动态调用工具**。

so --> *LangChain 负责的工具调用编排，现在模型自己就能做了。*

## 传统 Agent 的架构困境

所有大模型的 Agent 能力都面临一个根本性矛盾：

- **Chain-of-Thought（CoT）推理模式：** 能进行多步复杂推理，但推理过程是封闭的，无法中断去调用外部工具。
- **Function Calling（工具调用）模式：** 能执行外部操作，但每次调用都会打断推理链路，导致上下文丢失和推理碎片化。

这种架构分离导致的结果是：要么闭卷推理（无实时数据支撑），要么开卷查询（缺乏深度分析）。


## DeepSeek 3.2 的技术突破

### 核心创新：推理过程中的动态工具调用

DeepSeek 3.2 实现了全球首个"Reasoning-in-Action"范式：

**架构对比：**

```ad-important
**传统 ReAct**：Thought → Action → Observation → Thought... 
			（推理与行动交替，上下文割裂）
**V3.2 新范式**：Continuous Reasoning [Tool Call in Reasoning Process]
			（工具调用内嵌于连续推理流）
```

**技术实现：**

- **reasoning_content 传递机制：保持完整推理链路的上下文连贯性**
- 自适应工具决策：模型在推理中自主判断工具调用时机和参数
- 双模式支持：思考模式（复杂任务）+ 非思考模式（快速响应

这种架构让模型具备了真正的"元认知"能力：知道自己的知识边界，主动寻求外部信息补充。


![[Pasted image 20251202202046.png]]


## 使用
API 文档：[https://api-docs.deepseek.com/zh-cn/guides/thinking_mode](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode)

### DeepSeek 3.2 调用
DeepSeek 模型支持思考模式：在输出最终回答之前，模型会先输出一段思维链内容，以提升最终答案的准确性。您可以通过以下任意一种方式，开启思考模式：

1. 设置 `model` 参数：`"model": "deepseek-reasoner"`
    
2. 设置 `thinking` 参数：`"thinking": {"type": "enabled"}`

如果用的是 OpenAI SDK，在设置 `thinking` 参数时，需要将 `thinking` 参数传入 `extra_body` 中：

```python
response = client.chat.completions.create(
	model="deepseek-chat", 
	# ...  
	extra_body={"thinking": {"type": "enabled"}}
	)
```


### API 参数

- **输入参数**：
    - `max_tokens`：模型单次回答的最大长度（含思维链输出），默认为 32K，最大为 64K。
    
- **输出字段**：
    - `reasoning_content`：思维链内容，与 `content` 同级，访问方法见[样例代码](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode#%E6%A0%B7%E4%BE%8B%E4%BB%A3%E7%A0%81)。
    - `content`：最终回答内容。
    - `tool_calls`: 模型工具调用。
    
- **支持的功能**：[Json Output](https://api-docs.deepseek.com/zh-cn/guides/json_mode)、[Tool Calls](https://api-docs.deepseek.com/zh-cn/guides/tool_calls)、[对话补全](https://api-docs.deepseek.com/zh-cn/api/create-chat-completion)，[对话前缀续写 (Beta)](https://api-docs.deepseek.com/zh-cn/guides/chat_prefix_completion)
    
- **不支持的功能**：FIM 补全 (Beta)
    
- **不支持的参数**：`temperature`、`top_p`、`presence_penalty`、`frequency_penalty`、`logprobs`、`top_logprobs`。请注意，为了兼容已有软件，设置 `temperature`、`top_p`、`presence_penalty`、`frequency_penalty` 参数不会报错，但也不会生效。设置 `logprobs`、`top_logprobs` 会报错。


### 思考模式工具调用
```python
import os
import json
from openai import OpenAI

# The definition of the tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_date",
            "description": "Get the current date",
            "parameters": { "type": "object", "properties": {} },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of a location, the user should supply the location and date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": { "type": "string", "description": "The city name" },
                    "date": { "type": "string", "description": "The date in format YYYY-mm-dd" },
                },
                "required": ["location", "date"]
            },
        }
    },
]

# The mocked version of the tool calls
def get_date_mock():
    return "2025-12-01"

def get_weather_mock(location, date):
    return "Cloudy 7~13°C"

TOOL_CALL_MAP = {
    "get_date": get_date_mock,
    "get_weather": get_weather_mock
}

def clear_reasoning_content(messages):
    for message in messages:
        if hasattr(message, 'reasoning_content'):
            message.reasoning_content = None

def run_turn(turn, messages):
    sub_turn = 1
    while True:
        response = client.chat.completions.create(
            model='deepseek-chat',
            messages=messages,
            tools=tools,
            extra_body={ "thinking": { "type": "enabled" } }
        )
        messages.append(response.choices[0].message)
        reasoning_content = response.choices[0].message.reasoning_content
        content = response.choices[0].message.content
        tool_calls = response.choices[0].message.tool_calls
        print(f"Turn {turn}.{sub_turn}\n{reasoning_content=}\n{content=}\n{tool_calls=}")
        # If there is no tool calls, then the model should get a final answer and we need to stop the loop
        if tool_calls is None:
            break
        for tool in tool_calls:
            tool_function = TOOL_CALL_MAP[tool.function.name]
            tool_result = tool_function(**json.loads(tool.function.arguments))
            print(f"tool result for {tool.function.name}: {tool_result}\n")
            messages.append({
                "role": "tool",
                "tool_call_id": tool.id,
                "content": tool_result,
            })
        sub_turn += 1

if __name__ == '__main__':
	client = OpenAI(
	    api_key=os.environ.get('DEEPSEEK_API_KEY'),
	    base_url=os.environ.get('DEEPSEEK_BASE_URL'),
	)
	
	# The user starts a question
	turn = 1
	messages = [{
	    "role": "user",
	    "content": "How's the weather in Hangzhou Tomorrow"
	}]
	run_turn(turn, messages)
	
	# The user starts a new question
	turn = 2
	messages.append({
	    "role": "user",
	    "content": "How's the weather in Hangzhou Tomorrow"
	})
	# We recommended to clear the reasoning_content in history messages so as to save network bandwidth
	clear_reasoning_content(messages)
	run_turn(turn, messages)
```

在 Turn 1 的每个子请求中，都携带了该 Turn 下产生的 `reasoning_content` 给 API，从而让模型继续之前的思考。`response.choices[0].message` 携带了 `assistant` 消息的所有必要字段，包括 `content`、`reasoning_content`、`tool_calls`。简单起见，可以直接用如下代码将消息 append 到 messages 结尾：

```
messages.append(response.choices[0].message)
```

在 Turn 2 开始时，我们建议丢弃掉之前 Turn 中的 `reasoning_content` 来节省网络带宽：

```
clear_reasoning_content(messages)
```