def maxDepth(root):
    if not root:
        return 0
    max_depth = [1]
    self.dfs(root, 1, max_depth)
    return max_depth[0]


def dfs(self, root, depth, max_depth):
    if max_depth[0] < depth:
        max_depth[0] = depth

    if root:
        for child in root.children:
            self.dfs(child, depth + 1, max_depth)
