import sys

sys.setrecursionlimit(10**6)


def rev_util(node,k):
    if k<=1 or node.next is None:
        return node,(node,node.next)
    curr,data=rev_util(node.next,k-1)
    curr.next=node
    return node,data


def reverse(head,k):
    prev=None
    res=None
    while head is not None:
        start,data=rev_util(head,k)
        start.next=data[1]
        if prev:
            prev.next=data[0]
        else:
            res=data[0]

        prev=start
        head=data[1]
    return res
