# 연결리스트를 뒤집는다
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before = head
        after = head
        arr = []
        while before != None :
            arr.append(before.val)
            before = before.next
        arr.reverse()
        
        idx = 0
        while after != None :
            after.val = arr[idx]
            after = after.next
            idx += 1
        
        return head