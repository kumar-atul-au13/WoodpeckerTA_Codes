# Implement a Stack using 2 Queues
# Queue Class
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
    def deque(self):
        if len(self.queue)==0:
            return None
        return self.queue.pop(0)
    def length(self):
        return len(self.queue)
# Stack Class
class Stack:
    def __init__(self):
        self.push_queue = Queue()
        self.pop_queue = Queue()
    def push(self, data):
        print('pushing %d to stack' % data)
        self.push_queue.enqueue(data)
    def pop(self):
        if self.push_queue.length() == 0:
            return None
        while self.push_queue.length() > 1:
            self.pop_queue.enqueue(self.push_queue.deque())
        self.push_queue, self.pop_queue = self.pop_queue, self.push_queue
        return self.pop_queue.deque()
stk = Stack()
list1 = "5 6 2 3"
for i in list1.split():
    # print("pushing", i)
    stk.push(int(i))
print(stk.pop())    # 3
print(stk.pop())    # 2
stk.push(9)
stk.push(73)
print(stk.pop())    # 73
print(stk.pop())    # 9
print(stk.pop())    # 6
print(stk.pop())    # 5
print(stk.pop())    # Stack is empty!!!