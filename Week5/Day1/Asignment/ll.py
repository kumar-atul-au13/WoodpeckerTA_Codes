class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class linkedlist:
    def __init__(self,lst=[]):
        pass

    def display(self):
        curr_node=self.head
        while curr_node is not None:
            print('\033[46m',curr_node.data,'\033[41m',end=" --\033[0m-->")
            curr_node=curr_node.next
        else:
            print('\033[44m',"None",'\033[0m')
            print()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def head_ll(data=[]):
    head=None
    tail=None
    for x in data:
        if head==None:
            head=Node(x)
            tail=head
            continue
        new=Node(x)
        tail.next=new
        tail=tail.next
    return  head

def display_head(head,name=None):
    curr_node=head
    if name:
        print('\033[44m',name,'\033[0m',end="-\033[0m-->")
    while curr_node is not None:
        print('\033[46m',curr_node.data,'\033[41m',end=" --\033[0m-->")
        curr_node=curr_node.next
    else:
        print('\033[44m',"None",'\033[0m')
        print()

ll=linkedlist([5,4,5,6,1,5,2,6])
ll.display()
display_head( head_ll([5,4,5,6,1,5,2,6][::-1]))
