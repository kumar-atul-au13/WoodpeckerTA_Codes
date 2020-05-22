# You are given a circular linked list, write the code for:
# Inserting an element at a given position in the list
#Video-[15:00] https://drive.google.com/open?id=1BBJlXXAPPSJlAY3TdSJRjnPIs5JPxK0o
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def ins_position_cll(head,data,pos):
    temp=head
    if pos==1:
        while temp.next is not head:
            temp=temp.next
        new=Node(data)
        new.next=head
        temp.next=new
        head=new
        return head

    while pos>2:
        temp=temp.next
        pos-=1
        if temp.next is head and pos>2:
            print("Invalid Position")
            return
    new=Node(data)
    new.next=temp.next
    temp.next=new
    return head

