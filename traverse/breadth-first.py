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

    def breadth_first_iterator(self):
        q = queue.Queue()
        q.put(self.root)

        while not q.empty():
            node = q.get()
            yield node.payload
            for child in node.children:
                q.put(child)



def create_sample_tree():
    root = Tree("Root")
    for i in range(3):
        child1 = TreeNode("Child{}".format(i + 1))
        for j in range(4):
            child2 = TreeNode("Grandchild{}_{}".format(i + 1, j + 1))
            child1.add_child(child2)
            for k in range(2):
                child3 = TreeNode("GGC{}_{}_{}".format(i + 1, j + 1, k+1))
                child2.add_child(child3)

        root.root.add_child(child1)
    # print(root.root.children)


    return root

if __name__ == "__main__":
    tree = create_sample_tree()
    print("\nBreadth-first traversal:")
    for item in tree.breadth_first_iterator():
        print(item)