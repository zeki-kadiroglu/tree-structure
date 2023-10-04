from collections import deque
from src.nodeTree import TreeNode
from src.traverse.base import BaseTree

class ZigZag(BaseTree):
    def __init__(self, payload=0, children=None):
        self.payload = payload
        self.children = children if children is not None else []

    def iterate_traversal(self):
        if not self:
            return []

        result = []
        queue = deque([self])
        reverse_order = False

        while queue:
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.payload)

                for child in node.children:
                    queue.append(child)

            if reverse_order:
                level = level[::-1]

            result.append(level)
            reverse_order = not reverse_order

        return result



if __name__ == "__main__":
    
    # Create a generic tree based on a given structure
    def create_tree():
        root = TreeNode(1)
        child2 = TreeNode(2)
        child3 = TreeNode(3)
        root.add_child(child2)
        root.add_child(child3)
        
        gchild1 = TreeNode(4)
        
        child2.add_child(gchild1)
        
        child2.add_child(TreeNode(5))

        child3.add_child(TreeNode(6))
        child3.add_child(TreeNode(7))
        child3.add_child(TreeNode(8))  # Adding a third child to node 3

        # Add a level
        child4 = TreeNode(9)
        child5 = TreeNode(10)
        #child2.addChild(child4)
        child2.add_child(child5)

        # Add one more node
        child6 = TreeNode(11)
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