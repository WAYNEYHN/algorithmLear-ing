# class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    #
    # 
    # @param head ListNode类 
    # @param n int整型 
    # @return ListNode类
    def removeNthFromEnd(self , head , n ):
        # write code here
        if head == None:
            return None
        pre = None
        pres = head
        pNode = head
        while n>0:
            if pNode != None:
                pNode = pNode.next
            else:
                return None
            n -= 1
        if pNode == None:
            return head.next
        while pNode != None:
            pNode = pNode.next
            pre = pres
            pres = pres.next
        pre.next = pres.next
        return head