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

def display_head(head,name=None,reverse=None,ending=None):
    def rev_util(arr):
        if reverse:
            arr=list(map(lambda x:x[::-1],arr))
        return arr
    curr_node=head
    ans_str=""
    if name:
        ans_str+=" ".join(rev_util(['\033[44m',name,'\033[0m',"-\033[0m-->"]))
    while curr_node is not None:
        ans_str+=" ".join(rev_util(['\033[46m',str(curr_node.data),'\033[41m'," --\033[0m-->"]))
        curr_node=curr_node.next
    ans_str+=" ".join(rev_util(['\033[44m',"None",'\033[0m']))
    if reverse:
        ans_str=ans_str[::-1]
    if ending:
        print(ans_str,end=ending)
    else:
        print(ans_str)
    print()
display_head(head_ll([1,2,3,4,5]),name="head")
#-------------CODES START HERE----------METHOD 1---------------------
def reverse_util1(node,curr_head):
    temp=node.next
    node.next=curr_head
    if temp is not None:
        return reverse_util1(temp,node)
    return node
# def reverseList1(self):
#     # Code here
#     if self.head is None:
#         return None
#     self.head=reverse_util1(self.head,None)

display_head(reverse_util1(head_ll([1,2,3,4,5,6,7]),None),"Reversed")

#--------------METHOD 2--------------------------------
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
    # Code here MAKE SELF.HEAD
    if head is None:
        return None
    up_tail=reverse_util(head)

    return up_head
display_head(reverseList(head_ll([1,2,3,4,5,6,7])),"Reversed")