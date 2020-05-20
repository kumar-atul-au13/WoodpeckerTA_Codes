# ou are given a circular linked list, write the code for:
# Deleting an element at a given position in the list

def del_position_cll(head,pos):
    temp=head
    if pos==1:
        while temp.next is not head:
            temp=temp.next
        temp.next=temp.next.next
        head=temp.next
        return head
    while pos>2:
        temp=temp.next
        pos-=1
        if temp.next.next is head and pos>2:
            print("Invalid Position")
            return
    temp.next=temp.next.next
    return head