#Question-https://www.geeksforgeeks.org/pairwise-swap-elements-of-a-given-linked-list/
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
#------------------------------Program begins from here------METHOD-1------------------
def pairWiseSwap(head):
    if not head:
        return
    if not head.next:
        return head
    returned_head=pairWiseSwap(head.next.next)
    new_head=head.next
    new_head.next=head
    head.next=returned_head
    # display_head(pairWiseSwap(new_head))
    return new_head
display_head(pairWiseSwap( head_ll([7,8,9,1,2,3,4,5,6])))

#-----------------------------METHOD 2--------------------------------

# def pairWiseSwap(head):


