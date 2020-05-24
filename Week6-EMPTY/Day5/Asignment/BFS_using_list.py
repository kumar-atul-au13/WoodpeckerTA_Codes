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
    while queue.peek():
        queue.display_head()
        curr_vert=queue.dequeue()
        if curr_vert in visited:
            continue
        else:
            print(curr_vert)
            visited.add(curr_vert)
        for adj_vert in graph[curr_vert]:
            if adj_vert not in visited:
                queue.enqueue(adj_vert)


bfs(graph,'A')
        
