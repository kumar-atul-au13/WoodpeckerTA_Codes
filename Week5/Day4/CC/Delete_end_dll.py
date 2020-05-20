def del_end_dll(head):
    if not head or head.next is None:
        return None
    temp=head
    while temp.next.next is not None:
        temp=temp.next
    temp.next=None
    return head