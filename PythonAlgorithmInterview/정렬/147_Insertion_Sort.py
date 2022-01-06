# 148번과 같이 정렬로 풀어도 답이 된다
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

# 삽입 정렬
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 초깃값 변경
        cur = parent = ListNode(0)
        while head :
            while cur.next and cur.next.val < head.val :
                cur = cur.next
            
            cur.next, head.next, head = head, cur.next, head.next
            
            # 필요한 경우에만 cur 포인터가 되돌아가도록 처리
            if head and cur.val > head.val :
                cur = parent
        
        return parent.next