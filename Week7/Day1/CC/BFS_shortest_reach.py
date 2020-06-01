# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem?h_r=internal-search
#[ALTARNATE SOLUTION] https://github.com/anik-ghosh-au7/flamingo-woodpecker-attainU/blob/master/Solutions/Week%207/Day%201/w7d1cc1.py
from collections import defaultdict
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
def bfs(graph,vertex,n):
    # print(graph)
    result=[-1]*(n+1)
    visited=set()
    queue=Queue()
    queue.enqueue(vertex)
    visited.add(vertex)
    queue.enqueue("next_level")
    level=6
    while queue.peek():
        curr_vert=queue.dequeue()
        if curr_vert=="next_level":
            level+=6
            continue
        for adj_vert in graph[curr_vert]:
            if adj_vert not in visited:
                queue.enqueue(adj_vert)
                visited.add(adj_vert)
                result[adj_vert]=level
        if queue.peek()=="next_level":
            queue.enqueue("next_level")
    return result

def find_all_distances(graph,s,n):
    result=bfs(graph,s,n)

    for vertex in range(1,n+1):
        if vertex==s:
            continue
        print(result[vertex],end=" ")
    print()

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = defaultdict(dict)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph[x][y]=6
        graph[y][x]=6
    s = int(input())
    find_all_distances(graph,s,n)
