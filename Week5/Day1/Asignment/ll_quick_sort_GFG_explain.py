#Question-https://www.geeksforgeeks.org/quicksort-on-singly-linked-list/
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
def quickPart(head):
    if head.next is None:
        return None,None
    # display_head(head,"head")
    partion_elem=head
    curr_elem=head.next
    left_part=None
    right_part=None
    while curr_elem:
        # print(curr_elem.data)
        temp=curr_elem.next
        if curr_elem.data<partion_elem.data:
            if left_part==None:
                left_part=curr_elem
                curr_elem.next=None
            else:
                curr_elem.next=left_part
                left_part=curr_elem
            # display_head(left_part,"LeftPart")
        else:
            if right_part is None:
                right_part=curr_elem
                right_part.next=None
            else:
                curr_elem.next=right_part
                right_part=curr_elem
            # display_head(right_part,"RightPart")
        curr_elem=temp
    # display_head(left_part,"LeftPart")
    # display_head(right_part,"RightPart")
    return left_part,right_part

def quickSort(head):
    if head is None:
        return None
    pivot=head
    left_part,right_part=quickPart(head)
    left_part= quickSort(left_part)
    right_part= quickSort(right_part)

    #Print-Always sorted
    pivot.next=right_part
    left_tail=left_part
    if left_tail:
        while left_tail.next:
            left_tail=left_tail.next
        left_tail.next=pivot
    else:
        left_part=pivot
    # display_head(left_part,"Returning")
    return left_part


display_head(head_ll([10,4,6,22,3,11,4,5,90]),"HEAD")
display_head(quickSort(head_ll([10,4,6,22,3,11,4,5,90])),"Sorted")