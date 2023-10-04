class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, root_payload):
        self.root = TreeNode(root_payload)

    def create_tree(self, root_value, depth, branching_factor):
        if depth == 0:
            return Tree(root_value)

        root = TreeNode(root_value)
        for i in range(0, branching_factor+1):
            child_value = root_value + str(i) + "1"
            root.add_child(self.create_tree(child_value, depth - 1, branching_factor))

        return root

# Helper function to print the tree structure
def print_tree(node, level=1):
    if node is not None:
        print("  " * level + str(node.value))
        for child in node.children:
            print_tree(child, level + 1)

# Example usage:
t = TreeNode("root")
root = t.create_tree("root", 4 ,3)
# root = create_tree("root", 4, 3)
print("Tree Structure:")
print_tree(root)
