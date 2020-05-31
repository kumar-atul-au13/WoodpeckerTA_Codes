#video https://drive.google.com/file/d/1btERkgmo2f8Rv2OT2DlKmgYk_26vMptE/view?usp=sharing
from collections import defaultdict

#can have character also as a vertex
adj_lst=defaultdict(list)


def directed_matrix_to_list(matrix):
    v=len(matrix)
    for vertex in range(v):
        for adj_vert in range(v):
            if matrix[vertex][adj_vert]==1:
                adj_lst[vertex].append(adj_vert)# adj_lst["kgfdsgklg"]


matrix_representation=[
   # 0 1 2 3 4
    [0,1,0,1,0],#0
    [1,0,1,0,1],#1
    [0,1,0,1,0],#2
    [1,0,1,0,0],#3
    [0,1,0,0,0],#4
]
directed_matrix_to_list(matrix_representation)
print(adj_lst)
