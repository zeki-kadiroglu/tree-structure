from collections import deque

class Node:
    def __init__(self, key):
        self.val = key
        self.child = []

    def addChild(self, child_node):
        self.child.append(child_node)

class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []

    def zigzagLevelOrder(self):
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
                level.append(node.val)

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
        root = Node(1)
        child2 = Node(2)
        child3 = Node(3)
        root.addChild(child2)
        root.addChild(child3)
        
        gchild1 = Node(4)
        
        child2.addChild(gchild1)
        
        child2.addChild(Node(5))

        child3.addChild(Node(6))
        child3.addChild(Node(7))
        child3.addChild(Node(8))  # Adding a third child to node 3

        # Add an additional level
        child4 = Node(9)
        child5 = Node(10)
        #child2.addChild(child4)
        child2.addChild(child5)

        # Add one more node
        child6 = Node(11)
        gchild1.addChild(child6)
        gchild1.addChild(child4)

        return root

    # Convert to TreeNode for zigzagLevelOrder traversal
    def convert_to_tree_node(node):
        if not node:
            return None
        tn = TreeNode(node.val)
        for child in node.child:
            tn.children.append(convert_to_tree_node(child))
        return tn

    tree_root = convert_to_tree_node(create_tree())

    # Perform zigzag level order traversal
    result = tree_root.zigzagLevelOrder()

    # Print the result
    for level in result:
        print(level)