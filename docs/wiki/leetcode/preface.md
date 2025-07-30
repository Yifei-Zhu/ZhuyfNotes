---
layout: page
title: Recommended Learning Resources
author: Yifei Zhu
comments: true
tags:
 - Programming
 - LeetCode
 - Python
---

## Time Complexity

| Time Complexity | Typical Algorithms                     | LeetCode Examples                                                                 |
|-----------------|----------------------------------------|-----------------------------------------------------------------------------------|
| O(1)            | Constant-time operations (e.g., array indexing) | Most hash table operations (e.g., the hash solution for [1. Two Sum](https://leetcode.com/problems/two-sum/)) |
| O(log n)        | Binary search, fast exponentiation     | [704. Binary Search](https://leetcode.com/problems/binary-search/), [50. Pow(x, n)](https://leetcode.com/problems/powx-n/) |
| O(n)            | Linear traversal                       | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) |
| O(n log n)      | Efficient sorting algorithms           | [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) (QuickSort) |
| O(n²)           | Nested loops                           | Brute-force solution for [1. Two Sum](https://leetcode.com/problems/two-sum/) |
| O(2^n)          | Exponential recursion                  | [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) (backtracking) |

### 分析时间复杂度的实例


**LeetCode 704 - Binary Search：在一个排序数组中查找目标值，返回其索引**

- 算法每次将搜索范围减半（通过比较中间元素）。
- 假设数组长度为 n，第一次处理 n 个元素，第二次 n/2，第三次 n/4，...。
- 迭代次数为 $ \log_2 n $（因为 $ n / 2^k = 1 $，解得 $ k = \log_2 n $）。
- 每次迭代的操作（如比较、更新指针）是 O(1)。
- 总时间复杂度：O(log n)


## Categories of LeetCode Problems

**Status: 0 - GG 1 - Seen 2 - Basic 3 - Mastered**

### 1 Array (including Binary search)


| #   | Problem Name                     | Difficulty | 主要考点/解决方法 | Status |
|-----|----------------------------------|------------|------------------|--------|
| 704 | Binary Search                    | Easy       | 二分查找算法 | 2      |
| 27  | Remove Element                   | Easy       | 双指针（快慢指针） | 2      |
| 977 | Squares of a Sorted Array        | Easy       | 双指针（首尾指针） | 2      |
| 209 | Minimum Size Subarray Sum        | Medium     | 滑动窗口 | 1      |
| 59  | Spiral Matrix II                 | Medium     | 模拟、边界控制 |    1    |
| 44  | Wildcard Matching                | Hard       | 动态规划/回溯 |   0     |
| 58  | Length of Last Word              | Easy       | 字符串处理 |    2    |
| 1365| How Many Numbers Are Smaller     | Easy       | 排序+哈希/计数排序 |    1    |
| 941 | Valid Mountain Array             | Easy       | 双指针/单次遍历 |        |
| 1207| Unique Number of Occurrences     | Easy       | 哈希表统计频率 |        |
| 283 | Move Zeroes                      | Easy       | 双指针（快慢指针） |        |
| 189 | Rotate Array                     | Medium     | 数组反转技巧 |        |
| 724 | Find Pivot Index                 | Easy       | 前缀和 |        |
| 34  | Find First and Last Position     | Medium     | 二分查找（边界处理） |        |
| 35  | Search Insert Position           | Easy       | 二分查找 |        |
| 922 | Sort Array By Parity II          | Easy       | 双指针（奇偶指针） |        |


### 2 Linked List

| #   | Problem Name                     | Difficulty | 主要考点/解决方法 | Status |
|-----|----------------------------------|------------|------------------|--------|
| 203 | Remove Linked List Elements      | Easy       | 虚拟头节点+遍历删除 |        |
| 707 | Design Linked List               | Medium     | 链表基本操作实现 |        |
| 206 | Reverse Linked List              | Easy       | 迭代/递归反转 |        |
| 24  | Swap Nodes in Pairs              | Medium     | 虚拟头节点+双指针交换 |        |
| 19  | Remove Nth Node From End of List | Medium     | 快慢指针 |        |
| 160 | Intersection of Two Linked Lists | Easy       | 双指针走两轮 |        |
| 234 | Palindrome Linked List           | Easy       | 快慢指针找中点+反转后半部分 |        |
| 143 | Reorder List                     | Medium     | 找中点+反转+合并 |        |
| 141 | Linked List Cycle                | Easy       | 快慢指针判环 |        |


### 3 Hash Table


| #    | Problem Name                              | Difficulty | 主要考点/解决方法 | Status |
|------|-------------------------------------------|------------|------------------|--------|
| 242  | Valid Anagram                             | Easy       | 哈希表统计字符频率 |        |
| 1002 | Find Common Characters                   | Easy       | 多哈希表统计最小频率 |        |
| 349  | Intersection of Two Arrays                | Easy       | 哈希集合求交集/双指针 |        |
| 202  | Happy Number                              | Easy       | 哈希检测循环/快慢指针 |        |
| 1    | Two Sum                                   | Easy       | 哈希表存储补数 |        |
| 15   | 3Sum                                      | Medium     | 排序+双指针 |        |
| 383  | Ransom Note                               | Easy       | 哈希表字符计数 |        |
| 18   | 4Sum                                      | Medium     | 排序+双指针+两层循环 |        |
| 205  | Isomorphic Strings                        | Easy       | 双哈希表字符映射 |        |

### 4 String

| #    | Problem Name                              | Difficulty | 主要考点/解决方法 | Status |
|------|-------------------------------------------|------------|------------------|--------|
| 344  | Reverse String                            | Easy       | 双指针原地交换 |        |
| 541  | Reverse String II                         | Easy       | 分段反转+边界处理 |        |
| 151  | Reverse Words in a String                 | Medium     | 整体反转+单词反转 |        |
| 459  | Repeated Substring Pattern                | Easy       | KMP算法/字符串匹配 |        |
| 28   | Find the Index of the First Occurrence    | Medium     | KMP算法/暴力匹配 |        |
| 884  | Uncommon Words from Two Sentences        | Easy       | 哈希表统计词频 |        |
| 925  | Long Pressed Name                         | Easy       | 双指针字符比对 |        |


### 5 Stack and Queue
### 6 Tree
### 7 Backtracking
### 8 Greedy
### 9 Dynamic Programming
### 10 Graph
### 11 Advanced Data Structures
### 12 Other Algorithms

-  Bitwise Operation: 1356

These problems involve specialized data structures like tries, segment trees, binary indexed trees (BIT), or union-find (disjoint set).

**Example:**Search in Rotated Sorted Array, Reverse Bits, Palindrome Number.

