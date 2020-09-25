def has_cycle(head):
    slow= head
    fast= head
    flag=0
    if head is None:
        return 

    while(slow and fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False

