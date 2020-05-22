#Video:[25:00]https://drive.google.com/open?id=1BBJlXXAPPSJlAY3TdSJRjnPIs5JPxK0o
def del_end_dll(head):
    if not head or head.next is None:
        return None
    temp=head
    while temp.next.next is not None:
        temp=temp.next
    temp.next=None
    return head