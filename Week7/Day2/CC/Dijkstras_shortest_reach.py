# https://www.hackerrank.com/challenges/dijkstrashortreach/problem
import heapq

from collections import defaultdict
# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    graph=defaultdict(dict)
    for v1,v2,w in edges:
        if v2 not in graph[v1]:
            graph[v1][v2]=w
            graph[v2][v1]=w
        elif graph[v1][v2]>w:
            graph[v1][v2]=w
            graph[v2][v1]=w
    # print(graph)
    result=[-1]*(n+1)
    lst_for_hp=[] #prone
    heapq.heappush(lst_for_hp,(0,s))
    infected_set=set()
    while len(lst_for_hp)>0:
        print(lst_for_hp)
        poped_vertex = heapq.heappop(lst_for_hp)
        vertex=poped_vertex[1]
        tweight=poped_vertex[0] #total weight is the weight of the path
        if vertex in infected_set:
            continue
        result[vertex]=tweight
        print(vertex,tweight)
        infected_set.add(vertex)
        for adj_vertex, weight in graph[vertex].items(): #Travarese all adjacent vertex
            if adj_vertex not in infected_set:           #If not visited then push in heap
                heapq.heappush(lst_for_hp,(tweight+weight,adj_vertex))
    return result[1:s]+result[s+1:]