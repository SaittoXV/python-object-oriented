class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
def inorder(node):
    if node:
        inorder(node.left)
        print(node)
        inorder(nide.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
inorder(root)

