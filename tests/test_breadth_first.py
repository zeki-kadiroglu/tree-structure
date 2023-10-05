from src.nodeTree import TreeNode
from src.traverse.breadth_first import BreadthFirst

if __name__ == "__main__":
    def create_sample_tree():
        root = BreadthFirst("Root")
        child1 = TreeNode(1)
        child2 = TreeNode(2)
        child3 = TreeNode(3)

        root.root.add_child(child3)
        root.root.add_child(child2)
        root.root.add_child(child1)

        gchild1 = TreeNode(4)
        gchild2 = TreeNode(5)
        gchild3 = TreeNode(10)

        child3.add_child(gchild1)
        child3.add_child(gchild2)
        child3.add_child(gchild3)

        gchild4 = TreeNode(6)
        gchild5 = TreeNode(7)
        gchild6 = TreeNode(8)

        child2.add_child(gchild4)
        child2.add_child(gchild5)
        child2.add_child(gchild6)


        ggchild1 = TreeNode(9)
        ggchild2 = TreeNode(11)
        ggchild3 = TreeNode(12)

        gchild4.add_child(ggchild1)
        gchild4.add_child(ggchild2)
        gchild4.add_child(ggchild3)
        return root

    tree = create_sample_tree()
    print("\nBreadth-first traversal:")
    for item in tree.iterate_traversal():
        print(item)