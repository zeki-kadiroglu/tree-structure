import queue
from typing import Any

from src.nodeTree import TreeNode
from src.traverse.base import BaseTree

class BreadthFirst(BaseTree):
    def __init__(self, root_payload: Any):
        self.root = TreeNode(root_payload)

    def iterate_traversal(self):
        # create queue
        que = queue.Queue()
        # root added the queue
        que.put(self.root)
        # loop until que is empty
        while not que.empty():
            # dequeues a node from the queue using
            node = que.get()
            # yields the payload of the current node using
            yield node.payload
            # terates over the children of the current node (assuming that node.children is a list of child nodes).
            for child in node.children:
                # Each child node is adding the end of the queue.
                que.put(child)






