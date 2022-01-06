class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 리스트 내부에 요소를 정렬한다
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head 
        arr = []
        while node != None :
            arr.append(node.val)
            node = node.next
        
        node = head
        arr.sort()
        idx = 0
        while node != None :
            node.val = arr[idx]
            node = node.next
            idx += 1
        
        return head