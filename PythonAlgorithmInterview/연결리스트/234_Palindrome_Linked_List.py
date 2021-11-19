# 링크드 리스트 내의 내용을 탐색하여, 해당 탐색 결과가 회문인지 검사한다
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = ""
        while head != None :
            stack += str(head.val)
            head = head.next
        
        if stack == stack[::-1] :
            return True
        else :
            return False