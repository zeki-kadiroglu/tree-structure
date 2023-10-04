import queue

class TreeNode:
    def __init__(self, payload):
        self.payload = payload
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, root_payload):
        self.root = TreeNode(root_payload)

    def depth_first_iterator(self):
        def dfs(node):
            yield node.payload # visited node
            for child in node.children: # iterate children of current node
                yield from dfs(child) # continues through the children of current node
        return dfs(self.root)



def create_sample_tree():
    root = Tree("Root")
    for i in range(3):
        child1 = TreeNode("Child{}".format(i + 1))
        for j in range(4):
            child2 = TreeNode("Grandchild{}_{}".format(i + 1, j + 1))
            child1.add_child(child2)
            for k in range(2):
                child3 = TreeNode("GCTorun{}{}{}".format(i+1, j+1, k + 1))
                child1.add_child(child3)
            root.root.add_child(child1)
    return root

if __name__ == "__main__":
    tree = create_sample_tree()

    print("Depth-first traversal:")
    for item in tree.depth_first_iterator():
        print(item)