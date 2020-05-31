# Implement a Queue using Singly Linked List with both operations in O(1)
# Video:[10:00] https://drive.google.com/open?id=1C5x6v5mWBkRdGLqTHNGICRmN7TPpXBtq
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
    return  head,tail

class queue:
    def __init__(self,arr=[]):
        self.head,self.tail=head_ll(arr)
    def dequeue(self):
        if self.head:
            res=self.head.data
            self.head=self.head.next
            return res
    def enqueue(self,data):
        if not self.head:
            self.head=Node(data)
            self.tail=self.head
            return
        self.tail.next=Node(data)
        self.tail=self.tail.next

qu=queue([2,3,4])
print(qu.dequeue())#2
print(qu.dequeue())#3
print(qu.dequeue())#4
print(qu.dequeue())#None
qu.enqueue(22)
qu.enqueue(33)
print(qu.dequeue())#22
print(qu.dequeue())#33
print(qu.dequeue())#None