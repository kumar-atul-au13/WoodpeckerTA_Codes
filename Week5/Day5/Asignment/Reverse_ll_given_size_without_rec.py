def reverse(head,k):
    prev_tail=None
    res=None
    next_head=head
    while next_head:
        up_tail=next_head
        count=1
        tempa=next_head
        tempb=next_head.next
        while tempb and count<k:
            tempc=tempb.next
            tempb.next=tempa
            tempa,tempb,=tempb,tempc
            count+=1
        up_head=tempa
        if prev_tail:
            prev_tail.next=up_head
        prev_tail=up_tail
        if not res:
            res=up_head
        prev_tail.next=None
        next_head=tempb
    return res