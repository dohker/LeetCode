class Solution:
    def __init__(self):
        self.start_path = []
        self.dest_path = []

    def find_path(self, root, target, path):
        if root is None:
            return False

        path.append(root)

        if root.val == target:
            return True

        if (root.left and self.find_path(root.left, target, path)) or (
                root.right and self.find_path(root.right, target, path)):
            return True

        path.pop()
        return False

    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        self.find_path(root, startValue, self.start_path)
        self.find_path(root, destValue, self.dest_path)

        # Find common prefix length
        i = 0
        while i < len(self.start_path) and i < len(self.dest_path) and self.start_path[i] == self.dest_path[i]:
            i += 1

        # Steps to move up from startValue to the common ancestor
        steps_up = 'U' * (len(self.start_path) - i)

        # Steps to move down from the common ancestor to destValue
        steps_down = []
        current_node = self.start_path[i - 1]
        for node in self.dest_path[i:]:
            if current_node.left == node:
                steps_down.append('L')
            elif current_node.right == node:
                steps_down.append('R')
            current_node = node

        return steps_up + ''.join(steps_down)