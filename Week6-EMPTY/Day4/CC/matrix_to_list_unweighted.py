from collections import defaultdict
#can have character also as a vertex
adj_lst=defaultdict(list)
def directed_matrix_to_list(matrix):
    v=len(matrix)
    for vertex in range(v):
        for adj_vert in range(v):
            if matrix[vertex][adj_vert]==1:
                adj_lst[vertex].append(adj_vert)