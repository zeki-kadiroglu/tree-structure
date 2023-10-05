from src.nodeTree import TreeNode
from src.traverse.zigzag import ZigZag

if __name__ == "__main__":

    def create_tree():
        root = TreeNode("root")

        child1 = TreeNode(1)
        child2 = TreeNode(2)
        child3 = TreeNode(3)

        root.add_child(child2)
        root.add_child(child3)
        root.add_child(child1)

        gchild1 = TreeNode(4)

        child2.add_child(gchild1)
        child2.add_child(TreeNode(5))

        child3.add_child(TreeNode(6))
        child3.add_child(TreeNode(7))
        child3.add_child(TreeNode(8))  # Adding a third child to node 3

        # Add a level
        child4 = TreeNode(9)
        child5 = TreeNode(10)
        child2.add_child(child5)

        # Add one more node
        child6 = TreeNode(11)
        child7 = TreeNode(12)
        gchild1.add_child(child7)
        gchild1.add_child(child6)
        gchild1.add_child(child4)



        return root

    # Convert to ZigZag for zigzagLevelOrder traversal
    def convert_to_tree_node(node):
        if not node:
            return None
        tree_node = ZigZag(node.payload)
        for child in node.children:
            tree_node.children.append(convert_to_tree_node(child))
        return tree_node

    tree_root = convert_to_tree_node(create_tree())

    # Perform zigzag level order traversal
    result = tree_root.iterate_traversal()

    # Print the result
    for level in result:
        print(level)