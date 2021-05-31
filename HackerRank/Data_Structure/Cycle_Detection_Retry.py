def has_cycle(head):
    if head is None:
        return False
    else:
        slow = head
        fast = head.next
        while slow != fast :
            if (fast is None) or (fast.next is None):
                return False
            else:
                slow = slow.next
                fast = fast.next.next
        return True

# 참고
# https://github.com/abrahamalbert18/HackerRank-Solutions-in-Python/blob/master/Linked%20Lists:%20Detect%20a%20Cycle