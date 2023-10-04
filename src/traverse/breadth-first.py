import queue

from src.nodeTree import TreeNode

from src.traverse.base import BaseTree




class BreadthFirst(BaseTree):
    def __init__(self, root_payload):
        self.root = TreeNode(root_payload)

    def iterate_traversal(self):
        q = queue.Queue()
        q.put(self.root)

        while not q.empty():
            node = q.get()
            yield node.payload
            for child in node.children:
                q.put(child)





if __name__ == "__main__":
    
    tree = create_sample_tree()
    print("\nBreadth-first traversal:")
    for item in tree.breadth_first_iterator():
        print(item)
