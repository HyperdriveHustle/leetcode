# 输入两个链表，找出它们的第一个公共节点。 
# 
#  如下面的两个链表： 
# 
#  
# 
#  在节点 c1 开始相交。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, s
# kipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1
# ,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
#  
# 
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB =
#  1
# 输出：Reference of the node with value = 2
# 输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4
# ]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
#  
# 
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而
#  skipA 和 skipB 可以是任意值。
# 解释：这两个链表不相交，因此返回 null。
#  
# 
#  
# 
#  注意： 
# 
#  
#  如果两个链表没有交点，返回 null. 
#  在返回结果后，两个链表仍须保持原有的结构。 
#  可假定整个链表结构中没有循环。 
#  程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。 
#  本题与主站 160 题相同：https://leetcode-cn.com/problems/intersection-of-two-linked-lis
# ts/ 
#  
#  Related Topics 链表 
#  👍 147 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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

        
# leetcode submit region end(Prohibit modification and deletion)

# if __name__ == '__main__':
#     node0 = ListNode(0)
#     node1 = ListNode(1)
#     node2 = ListNode(2)
#     node3 = ListNode(3)
#     node4 = ListNode(4)
#     node5 = ListNode(5)
#
#     node0.next = node2
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#     node4.next = node5
#
#     pa = node1
#     pb = node0
#
#     ss = Solution()
#     res = ss.getIntersectionNode(pa, pb)
#     print(res.val)
