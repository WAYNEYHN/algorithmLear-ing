class Solution:
    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp


fib = lambda n: n if n < 2 else 2*fib(n-1)



class Solution:
    def reverseKGroup(self , head , k ):
        # write code here
        temp = head
        for _ in range(k):
            if temp is None:
                return head
            temp = temp.next
        last,temp = head, head
        #temp = head
        head = ListNode(0)
        for i in range(k):
            q = temp
            temp = temp.next
            q.next = head.next
            head.next = q
        last.next = self.reverseKGroup(temp, k)
        return head.next
print(fib(3))

l1 = ['b','c','d','b','c','a','a']
del l1[0]

print(l1)