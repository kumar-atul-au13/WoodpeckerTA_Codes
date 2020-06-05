#Video- Missed recording on june 4th
graph = {
    'A': {'B': 2, 'D': 4},
    'B': {'C': 1, 'A': 2},
    'D': {'A': 4, 'C': 3, 'E': 2, 'F': 11},
    'E': {'D': 2, 'F': 7},
    'F': {'D': 11, 'E': 7},
    'C': {'B': 1, 'D': 3, 'H': 2, 'G': 6},
    'G': {'C': 6, 'H': 2, 'I': 4},
    'H': {'C': 2, 'G': 2, 'I': 1},
    'I': {'G': 4, 'H': 1}
}

import heapq
lst_for_hp=[] #prone
# EDGE FORMAT x = (3,'a','b')  weight=x[0] starting_vertex = x[1] ending_vertex = x[2]

heapq.heappush(lst_for_hp,(0,"H",None))
infected_set=set()
answer_edge=[]
while len(lst_for_hp)>0:
    poped_edge = heapq.heappop(lst_for_hp)
    curr_vertex=poped_edge[1]
    if curr_vertex not in infected_set:
        infected_set.add(curr_vertex)
        answer_edge.append(poped_edge)
    else:
        continue
    for adj_vertex, weight in graph[curr_vertex].items():
        if adj_vertex not in infected_set:
            heapq.heappush(lst_for_hp,(weight,adj_vertex,curr_vertex))
print(answer_edge)
