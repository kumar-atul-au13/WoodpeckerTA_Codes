class Queue:
    def __init__(self):
        self.lst=[]
    def enque(self,data):
        print("Enquing ",data)
        self.lst.insert(0,data)
    def dequeue(self):
        if self.size()>0:
            return self.lst.pop()
    def peek(self):
        if self.size()>0:
            return self.lst[-1]
    def display(self):
        print(self.lst)
    def size(self):
        return len(self.lst)

queue=Queue()
print(queue.dequeue())
queue.enque(2)
queue.enque(3)
queue.enque(4)
queue.enque(5)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
queue.enque(6)
queue.enque(7)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
