from typing import Any

from src.nodeTree import TreeNode
from src.traverse.base import BaseTree

class DeepFirst(BaseTree):
    def __init__(self, root_payload: Any):
        self.root = TreeNode(root_payload)

    def iterate_traversal(self):
        def dfs(node):
            # visited node
            yield node.payload
            # iterate children of current node
            for child in node.children:
                # continues through the children of current node
                yield from dfs(child)
        return dfs(self.root)





