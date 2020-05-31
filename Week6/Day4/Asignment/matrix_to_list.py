#video[1:43] https://drive.google.com/file/d/1btERkgmo2f8Rv2OT2DlKmgYk_26vMptE/view?usp=sharing

from collections import defaultdict

adj_lst=defaultdict(dict)


def directed_matrix_to_list(matrix):
    v=len(matrix)
    for vertex in range(v):
        for adj_vert in range(v):
            if matrix[vertex][adj_vert] is not 0:
                adj_lst[vertex][adj_vert]=matrix[vertex][adj_vert]


matrix_representation=[
#    0  1  2  3  4
    [0 ,10,0 ,40,0 ],#0
    [10,0 ,20,0 ,50],#1
    [0 ,20,0 ,30,0 ],#2
    [40,0 ,30,0 ,0 ],#3
    [0 ,50,0 ,0 ,0 ],#4
]
directed_matrix_to_list(matrix_representation)
print(adj_lst)