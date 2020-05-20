class NodeD:
    def __init__(self,elem):
        self.prev=None
        self.next=None
        self.data=elem

def create_dll(lst):
    head=None
    tail=None
    for data in lst:
        if head is None:
            head=NodeD(data)
            tail=head
        else:
            new=NodeD(data)
            new.prev=tail
            tail.next=new
            tail=tail.next
    return head

def displayD(head,name=None):
    if not head:
        print(None)
        return
    curr_node=head
    if name:
        print('\033[44m',name,'\033[0m',end="-\033[0m-->")
    while curr_node.next is not None:
        print('\033[46m',curr_node.data,'\033[41m',end="<==\033[0m==\033[47m==>")
        curr_node=curr_node.next
    else:
        print('\033[46m',curr_node.data,'\033[41m',end="\033[0m\033[47m-->")
        print('\033[44m',"None",'\033[0m')
        print()
dll=create_dll([2,3])
displayD(dll,"head")
def del_end_dll(head):
    if not head or head.next is None:
        return None
    temp=head
    while temp.next.next is not None:
        temp=temp.next
    temp.next=None
    return head

# displayD(del_end_dll(dll),"head")

def del_pos_dll(head,pos):
    temp=head
    while pos>1 :
        temp=temp.next
        pos-=1
    prev_node=temp.prev
    next_node=temp.next
    if prev_node:
        prev_node.next=next_node
    else:
        head=next_node
    if next_node:
        next_node.prev=prev_node
    return head

dll=create_dll([2,3])
displayD(del_pos_dll(dll,2),"head")