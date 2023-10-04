class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

# Create the root node
root = TreeNode("Level 1")

# Add children to the root node
for i in range(3):
    child = TreeNode(f"Level 2 Child {i+1}")
    root.add_child(child)

    # Add children to the Level 2 nodes
    for j in range(3):
        grandchild = TreeNode(f"Level 3 Child {i+1}-{j+1}")
        child.add_child(grandchild)

        # Add children to the Level 3 nodes
        for k in range(3):
            great_grandchild = TreeNode(f"Level 4 Child {i+1}-{j+1}-{k+1}")
            grandchild.add_child(great_grandchild)

# Function to print the tree structure
def print_tree(node, level=0):
    prefix = "  " * level
    print(prefix + node.data)
    for child in node.children:
        print_tree(child, level + 1)

# Print the tree
print_tree(root)