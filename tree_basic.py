class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)

def topbottom(node):
    if node:
        print(node.value)
        topbottom(node.left)
        topbottom(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
inorder(root)
topbottom(root)

