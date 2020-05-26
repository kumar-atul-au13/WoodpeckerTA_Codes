#Question-https://www.hackerrank.com/challenges/queue-using-two-stacks/problem?isFullScreen=false
#Video-https://drive.google.com/open?id=1_MnnOOmWdcsaCCDZRkhkttyLENo6Qt8T
class stack:
    def __init__(self):
        self.lst=[]
    def push(self, data):
        self.lst.append(data)
    def pop(self):
        if len(self.lst)>0:
            return self.lst.pop()
    def peek(self):
        if len(self.lst)>0:
            return self.lst[-1]
# stk=stack()
# print(stk.pop())
# stk.push(33)
# stk.push(53)
# stk.push(3)
# print(stk.pop())
# print(stk.pop())
# print(stk.pop())
# print(stk.pop())

class queue:
    def __init__(self):
        self.enq_stack=stack()
        self.deq_stack=stack()
    def enqueue(self,data):
        self.enq_stack.push(data)
    def dequeue(self):
        res=self.deq_stack.pop()
        if res is not None:
            return res
        transfer=self.enq_stack.pop()
        while transfer:
            self.deq_stack.push(transfer)
            transfer=self.enq_stack.pop()
        return self.deq_stack.pop()
    def peek(self):
        # return self.
        if self.deq_stack.peek():
            return self.deq_stack.peek()
        transfer=self.enq_stack.pop()
        while transfer:
            self.deq_stack.push(transfer)
            transfer=self.enq_stack.pop()
        return self.deq_stack.peek()

qu=queue()
qu.enqueue(3)
qu.enqueue(4)
qu.enqueue(5)
print(qu.peek())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
qu.enqueue(3)
print(qu.dequeue())
qu.enqueue(4)
qu.enqueue(5)
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())


t=int(input())
qu=queue()
for _ in range(t):
    arr=[int(x) for x in input().split()]
    if arr[0]==1:
        qu.enqueue(arr[1])
    elif arr[0]==2:
        qu.dequeue()
    elif arr[0]==3:
        print(qu.peek())