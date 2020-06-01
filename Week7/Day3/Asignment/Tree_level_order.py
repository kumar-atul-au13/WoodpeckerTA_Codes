# https://www.hackerrank.com/challenges/tree-level-order-traversal
# Video-[27:00] https://drive.google.com/file/d/1r3KFYzndNJnRf8ydvSVShSn1-sUmldl4/view?usp=sharing
level_list=[]
def levelOrder_util(root,level):
    if len(level_list)<=level:
        level_list.append([])
    level_list[level].append(root.info)
    if root.left:
        levelOrder_util(root.left,level+1)
    if root.right:
        levelOrder_util(root.right,level+1)
def levelOrder(root):
    levelOrder_util(root,0)
    for ll in level_list:
        print(*ll,end=" ")
    print()
