# https://www.geeksforgeeks.org/reverse-a-linked-list/
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

up_head=None


def reverse_util(node):
    global up_head
    if node.next:
        nxt_node=reverse_util(node.next)
        nxt_node.next=node
    else:
        up_head=node
    node.next=None
    return node


def reverseList(head):
    # Code here
    if head is None:
        return None
    up_tail=reverse_util(head)

    return up_head
display_head(reverseList(head_ll([1,2,3,4,5,6,7])),"Reversed")