# Implement a Stack using Singly Linked List [optional]
#Video https://drive.google.com/open?id=1C5x6v5mWBkRdGLqTHNGICRmN7TPpXBtq
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        if self.top is None:
            self.top=Node(data)
        else:
            new=Node(data)
            new.next=self.top
            self.top=new
    def pop(self):
        if self.top:
            res=self.top.data
            self.top=self.top.next
            return res
    def peek(self):
        if self.top:
            res=self.top.data
            return res

stk=stack()
stk.push(4)
print(stk.pop())#4
print(stk.pop())#None
stk.push(5)
stk.push(6)
stk.push(7)
print(stk.pop())#7
print(stk.peek())#6
print(stk.pop())#6
print(stk.pop())#5
print(stk.peek())#None
print(stk.pop())#None
