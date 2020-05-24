from collections import defaultdict
adj_lst=defaultdict(dict)
def directed_matrix_to_list(matrix):
    v=len(matrix)
    for vertex in range(v):
        for adj_vert in range(v):
            if matrix[vertex][adj_vert] is not 0:
                adj_lst[vertex][adj_vert]=matrix[vertex][adj_vert]