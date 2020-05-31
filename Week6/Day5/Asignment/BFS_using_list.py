#video[6:00] https://drive.google.com/file/d/1btERkgmo2f8Rv2OT2DlKmgYk_26vMptE/view?usp=sharing

from queue import Queue
graph= {
    'A': {'B': 1, 'D': 4},
    'B': {'C': 1, 'A': 1},
    'D': {'A': 4, 'C': 1, 'E': 2, 'F': 11},
    'E': {'D': 2, 'F': 7},
    'F': {'D': 11, 'E': 7},
    'C': {'B': 1, 'D': 1, 'H': 2, 'G': 6},
    'G': {'C': 6, 'H': 2, 'I': 4},
    'H': {'C': 2, 'G': 2, 'I': 1},
    'I': {'G': 4, 'H': 1}
}
def bfs(graph,vertex):
    visited=set()
    queue=Queue()
    queue.enqueue(vertex)
    visited.add(vertex)
    while queue.peek():
        # queue.display_head()
        curr_vert=queue.dequeue()
        print(curr_vert)
        for adj_vert in graph[curr_vert]:
            if adj_vert not in visited:
                queue.enqueue(adj_vert)
                visited.add(adj_vert)


bfs(graph,'A')
        
