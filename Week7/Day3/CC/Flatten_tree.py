# https://www.geeksforgeeks.org/flatten-a-binary-tree-into-linked-list/
# Video-https://drive.google.com/file/d/1mY_eD62K7fc5UlWbPH_KIGKou1CLdtYy/view?usp=sharing
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.add_node(self.root, data)
    def add_node(self, node, data):
        if node.data < data:
            self.add_right(node, data)
        else:
            self.add_left(node, data)
    def add_right(self, node, data):
        if node.right is None:
            node.right = Node(data)
        else:
            self.add_node(node.right, data)
    def add_left(self, node, data):
        if node.left is None:
            node.left = Node(data)
        else:
            self.add_node(node.left, data)
def inOrder_traversal(root):    # root --> left --> right
    if root is None:
        print("None", end=" ")
        return
    print(root.data,end=" ")
    inOrder_traversal(root.left)
    inOrder_traversal(root.right)
def flatten(root):
    if not root:
        return None, None

    lstart,lend=flatten(root.left)
    rstart,rend=flatten(root.right)
    root.left=None
    if lstart and rstart:
        root.right=lstart
        lend.right=rstart
        end=rend
    elif lstart:
        root.right=lstart
        end=lend
    elif rstart:
        root.right=rstart
        end=rend
    else:
        end=root

    return root,end

tree = BinaryTree()
tree.add(3)
tree.add(5)
tree.add(1)
tree.add(8)
tree.add(2)
tree.add(4)
tree.add(6)
inOrder_traversal(tree.root)
flatten(tree.root)
print()
inOrder_traversal(tree.root)