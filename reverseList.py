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
print(fib(3))

l1 = ['b','c','d','b','c','a','a']
del l1[0]

print(l1)