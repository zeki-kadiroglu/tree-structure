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






