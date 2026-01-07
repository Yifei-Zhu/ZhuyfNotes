---
layout: page
title: LaTeX Tips
author: Yifei Zhu
comments: true
tags:
  - LaTeX
---
## \newcommand vs \renewcommand vs \providecommand

### Comparison Table

| Command | Behavior When Defined | Behavior When Undefined | Use Case |
|---------|----------------------|------------------------|----------|
| `\newcommand` | **Error** | Create new command | Ensure command uniqueness |
| `\renewcommand` | **Redefine** | Error | Force modify existing command |
| `\providecommand` | **Keep original** | Create new command | Safe definition, avoid conflicts |

## Detailed Explanation

### \newcommand
- **Purpose**: Define a new command with uniqueness guarantee
- **When to use**: When you want to ensure no command with the same name exists
- **Example**:
  ```latex
  \newcommand{\mycommand}[1]{\textbf{#1}}
  ```

### \renewcommand  
- **Purpose**: Redefine an existing command
- **When to use**: When you need to modify behavior of pre-defined commands
- **Example**:
  ```latex
  \renewcommand{\vec}[1]{\mathbf{#1}}  % Change vector notation to bold
  ```

#### \providecommand
- **Purpose**: Safely define a command without causing conflicts
- **When to use**: In packages/templates where command might be defined elsewhere
- **Example**:
  ```latex
  \providecommand{\zhtoday}{\CJK@today}  % Only define if not already defined
  ```

### Best Practices

1. **Use `\providecommand` in packages** for better compatibility
2. **Use `\newcommand` in documents** to catch naming conflicts early  
3. **Use `\renewcommand` cautiously** - know what you're overriding
4. **Always check command existence** in shared environments:
