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
        # check queue is true(not empty)
        while queue:
            level = []
            # detect number of nodes in the current level.
            level_size = len(queue)

            for _ in range(level_size):
                # dequeues nodes from the front of the queue
                node = queue.popleft()
                # appends their payload
                level.append(node.payload)
                # enqueues their children back into the queue.
                for child in node.children:
                    queue.append(child)

            if reverse_order:
                # reverse current level node list
                level = level[::-1]
            # result lists all level of the tree in the order, they were traversed. every other level will be reversed.
            result.append(level)
            reverse_order = not reverse_order

        return result


