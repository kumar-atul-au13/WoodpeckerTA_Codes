#Question-https://www.geeksforgeeks.org/quicksort-on-singly-linked-list/
#Video- https://drive.google.com/open?id=1fxhs1GEaFbzk6uylWmjleFhFJHCIgJwG
def addNode(head,node):
    if head:
        node.next=head
    else:
        node.next=None
    return node
def quickPart(head):
    if head.next is None:
        return None,None
    # display_head(head,"head")
    partion_elem=head
    curr_elem=head.next
    left_part=None
    right_part=None
    while curr_elem:
        temp=curr_elem.next
        if curr_elem.data<partion_elem.data:
            left_part=addNode(left_part,curr_elem)
        else:
            right_part=addNode(right_part,curr_elem)
        curr_elem=temp
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
    if left_tail is not None:
        while left_tail.next:
            left_tail=left_tail.next
        left_tail.next=pivot
    else:
        left_part=pivot
    return left_part