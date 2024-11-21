class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_recursively(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self.insert_recursively(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self.insert_recursively(current_node.right, value)

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.insert_recursively(self.root, value)

    
    def inorder_recursively(self, node):
        return (
            self.inorder_recursively(node.left) +
            [node.value] +
            self.inorder_recursively(node.right) if node else []
        )

    def inorder_traversal(self):
        return self.inorder_recursively(self.root)

    

if __name__ == "__main__":
    bt = BinaryTree()

    values = [7, 3, 9, 1, 5, 8, 10]
    
    for val in values: 
        bt.insert(val)

    print("inorder", bt.inorder_traversal())

    
