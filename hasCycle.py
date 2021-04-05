
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#         
#         
#判断列表是否有环
class Solution:
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        node1 = head
        node2 = head.next

        
        while node1 != node2:
            if node2 is None or node2.next is None:
                return False
            node1 = node1.next
            node2 = node2.next.next
        return True

        # while node2 != None or node2 != None:
        #     node1 = node1.next
        #     node2 = node2.next.next
        #     if node1 == node2:
        #         return True
        # return False
        # 

#链表中环的入口
class Solution:
    def detectCycle(self, head):
        if head is None or head.next is None:
            return False
        node1 = head
        node2 = head #快指针
        
        while node2 is None or node2.next is None:
            node1 = node1.next
            node2 = node2.next.next
            if node1 == node2:
                node3 = head
                while node3 != node1:
                    node3 =node3.next
                    node1 = node1.next
                return node1   #环的入口
        return None

# 快指针与慢指针均从X出发，在Z相遇。此时，慢指针行使距离为a+b，快指针为a+b+n(b+c）。
# 所以2*(a+b)=a+b+n*(b+c),推出
# a=(n-1)*b+n*c=(n-1)(b+c)+c;