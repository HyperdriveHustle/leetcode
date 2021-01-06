## 题目描述

输入两个链表，找出它们的第一个公共节点。 

**示例：**

输入：`intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1`

输出：Reference of the node with value = 2

输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 `[0,9,1,2,4]`，链表 B 为 `[3,2,4]`。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

注意： 


- 如果两个链表没有交点，返回 null. 
- 在返回结果后，两个链表仍须保持原有的结构。 
- 可假定整个链表结构中没有循环。 
- 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。 
- 本题与主站 160 题相同：https://leetcode-cn.com/problems/intersection-of-two-linked-lis
ts/ 

## 思路

- 方法一

分别遍历一遍，记录两个链表的长度，计算长度差值step。较长的先移动 step位，然后两个链表同时移动，遇到的第一个相同的节点即为相交点

- 方法二

使用栈，利用“先进后出”的思想，把两个链表分别压入栈中，从最后一个节点开始 pop，最后一个相同的节点即为相交的点

## code

```python
# 方法一
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        length_A, length_B = 0, 0
        pa, pb = headA, headB
        spa, spb = headA, headB
        # 获取 链表a 的长度
        while pa:
            pa = pa.next
            length_A += 1
        # 获取 链表b 的长度
        while pb:
            pb = pb.next
            length_B += 1

        if length_B > length_A:
            step = length_B - length_A
            while step:
                spb = spb.next
                step -= 1
        elif length_B < length_A:
            step = length_A - length_B
            while step:
                spa = spa.next
                step -= 1

        while spa and spb and spa != spb:
            spa = spa.next
            spb = spb.next
        return spa
```

方法二

```python
from collections import deque
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        stack_A, stack_B = deque(), deque()
        pa, pb = headA, headB
        while pa:
            stack_A.append(pa)
            pa = pa.next
        while pb:
            stack_B.append(pb)
            pb = pb.next

        pa = stack_A.pop()
        pb = stack_B.pop()
        if pa != pb:
            return None
        res = pa
        while stack_A and stack_B:
            pa = stack_A.pop()
            pb = stack_B.pop()
            if pa == pb:
                res = pa
            else:
                break
        return res
```
  