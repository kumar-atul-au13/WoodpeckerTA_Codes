def del_pos_dll(head,pos):
    temp=head
    while pos>1:
        temp=temp.next
    prev_node=temp.prev
    next_node=temp.next
    if prev_node:
        prev_node.next=next_node
    else:
        head=next_node
    if next_node:
        next_node.prev=prev_node
    return head