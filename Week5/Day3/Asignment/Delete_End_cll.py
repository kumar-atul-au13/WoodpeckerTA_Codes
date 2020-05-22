# You are given a circular linked list, write the code for
# Deleting an element at the end of the list
#Video: Forgot to start recording
def del_end_cll(head):
    if not head or head.next==head :
        return None
    temp=head
    while temp.next.next is not head:
        temp=temp.next
    temp.next=head
    return head



