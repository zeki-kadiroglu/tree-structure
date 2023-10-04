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

        while queue:
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.payload)

                for child in node.children:
                    queue.append(child)

            if reverse_order:
                level = level[::-1]

            result.append(level)
            reverse_order = not reverse_order

        return result


