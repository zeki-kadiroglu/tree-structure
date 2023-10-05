from src.nodeTree import TreeNode
from src.traverse.deep_first import DeepFirst

if __name__ == "__main__":
    def create_sample_tree():
        root = DeepFirst("Root")
        for i in range(3):
            child1 = TreeNode("Child{}".format(i + 1))
            for j in range(3):
                child2 = TreeNode("Grandchild{}_{}".format(i + 1, j + 1))
                child1.add_child(child2)
                for k in range(2):
                    child3 = TreeNode("GCTorun{}{}{}".format(i+1, j+1, k + 1))
                    child1.add_child(child3)
                root.root.add_child(child1)
        return root
    tree = create_sample_tree()

    print("Depth-first traversal:")
    for item in tree.iterate_traversal():
        print(item)