class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def create_cll(lst):
    head=None
    tail=None
    for data in lst:
        if head is None: #can be written as- if not head:
            head=Node(data)
            head.next=head
            tail=head
        else:
            new=Node(data)
            new.next=head
            tail.next=new
            tail=tail.next
    return head

def display_circular(head,name=None):
    if not head:
        return print(None)
    temp=head
    curr_node=head
    if name:
        print('\033[44m',name,'\033[0m',end="-\033[0m-->")
    else:
        print('\033[44m',"head",'\033[0m',end="-\033[0m-->")
    print('\033[46m',curr_node.data,'\033[41m',end=" --\033[0m-->")
    curr_node=curr_node.next
    while curr_node is not head:
        print('\033[46m',curr_node.data,'\033[41m',end=" --\033[0m-->")
        curr_node=curr_node.next
    else:
        print('\033[44m',"head "+str(head.data),'\033[0m')
        print()

cll=create_cll([2,4,6,7,8,2,3])
# display_circular(cll)

def del_end_cll(head):
    if not head or head.next==head :
        return None
    temp=head
    while temp.next.next is not head:
        temp=temp.next
    temp.next=head
    return head
# del1=del_end_cll(cll)
# display_circular(del1)
#
# del2=del_end_cll(cll)
# display_circular(del2)
#
# del3=del_end_cll(cll)
# display_circular(del3)
#
# del4=del_end_cll(cll)
# display_circular(del4)
#
# del5=del_end_cll(cll)
# display_circular(del5)
#
# del6=del_end_cll(cll)
# display_circular(del6)
#
# del7=del_end_cll(cll)
# display_circular(del7)

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
# display_circular(cll,"Initially")
# display_circular(del_position_cll(cll,7))

def ins_end_cll(head,data):
    if not head:
        new=Node(data)
        new.next=new
        return new
    temp=head
    while temp.next is not head:
        temp=temp.next
    new=Node(data)
    new.next=head
    temp.next=new
    return head
# cll=create_cll([2,4,5,7])
# display_circular(ins_end_cll(cll,8))

def ins_position_cll(head,data,pos):
    temp=head
    if pos==1:
        while temp.next is not head:
            temp=temp.next
        new=Node(data)
        new.next=temp.next
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

cll=create_cll([2,3,4])
display_circular(ins_position_cll(cll,100,4))