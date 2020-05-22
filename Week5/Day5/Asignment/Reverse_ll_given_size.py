#https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1
#Video:https://drive.google.com/open?id=1c7bufHB7FtL_91NGIB3Ju1enGB9sVigE
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
        up_tail,data=rev_util(head,k)
        up_tail.next=data[1]
        if prev:
            prev.next=data[0]
        else:
            res=data[0]

        prev=up_tail
        head=data[1]
    return res
