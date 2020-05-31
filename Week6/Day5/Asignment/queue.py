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

class Queue:
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
    def peek(self):
        if self.head:
            return self.head.data

    def display_head(self,head=None,name=None):
        curr_node=head
        if not head:
            curr_node=self.head
        if name:
            print('\033[44m',name,'\033[0m',end="-\033[0m-->")
        while curr_node is not None:
            print('\033[46m',curr_node.data,'\033[41m',end=" --\033[0m-->")
            curr_node=curr_node.next
        else:
            print('\033[44m',"None",'\033[0m')
            print()