
class TreeNode:
    def __init__(self, payload):
        self.payload = payload
        self.children = []

    def add_child(self, child):
        self.children.append(child)
