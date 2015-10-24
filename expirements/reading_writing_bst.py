class Node:
    def __init__(self):
        self.val = -1 
        self.left = None
        self.right = None


def preorder(root):
    if root == None:
        return
    print root.val
    preorder(root.left)
    preorder(root.right)





def build(arr, root, maxx, minn):
    if len(arr) == 0:
        return None
    val = arr[0]
    arr.remove(val)
    root.val = val
    if len(arr) != 0:
        root.left = build(arr, Node(), val, minn)
        root.right = build(arr, Node(), maxx, val)
    return root

def insert(tree, val):
    if tree == None:
        tree = Node()
        tree.val = val
        return tree
    if val > tree.val:
        tree.right = insert(tree.right, val)
    if val < tree.val:
        tree.left = insert(tree.left, val)
    return tree

arr = [30,20,10,40,35,50]
maxx = 9999
minn = 0
root = Node()
root.val = arr[0]
# build(arr, root, maxx, minn)
for i in arr[1:]:
    insert(root, i)

preorder(root)
    


    


