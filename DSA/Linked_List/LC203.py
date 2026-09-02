def removeElements(self, head, val):
        
        dummy = ListNode()
        dummy.next = head

        curr = dummy

        while curr and curr.next:

            if curr.next.val == val:

                curr.next = curr.next.next
            
            else:

                curr = curr.next
        
        return dummy.next