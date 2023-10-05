from src.nodeTree import TreeNode
from src.traverse.deep_first import DeepFirst

if __name__ == "__main__":
    def create_sample_tree():
        root = DeepFirst("Root")
        child1 = TreeNode(1)
        child2 = TreeNode(2)
        root.root.add_child(child1)
        root.root.add_child(child2)

        gchild1 = TreeNode(3)
        child1.add_child(gchild1)

        child1.add_child(TreeNode(5))

        child2.add_child(TreeNode(6))
        child2.add_child(TreeNode(7))
        child2.add_child(TreeNode(8)) # Adding a third child to node 3

        # Add a level
        child3 = TreeNode(9)
        child4 = TreeNode(10)
        child2.add_child(child3)

        # Add one more node
        child6 = TreeNode(11)
        gchild1.add_child(child6)
        gchild1.add_child(child3)

        # for i in range(3):
        #     child1 = TreeNode("Child{}".format(i + 1))
        #     for j in range(2):
        #         child2 = TreeNode("Grandchild{}_{}".format(i + 1, j + 1))
        #         child1.add_child(child2)
        #         for k in range(2):
        #             child3 = TreeNode("GCTorun{}{}{}".format(i+1, j+1, k + 1))
        #             child1.add_child(child3)
        #             break
        #         root.root.add_child(child1)
        return root
    tree = create_sample_tree()

    print("Depth-first traversal:")
    for item in tree.iterate_traversal():
        print(item)
