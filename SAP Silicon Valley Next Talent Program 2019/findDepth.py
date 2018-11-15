def maxDepth(root):
    if not root:
        return 0
    max_depth = [1]
    dfs(root, 1, max_depth)
    return max_depth[0]


def dfs(root, depth, max_depth):
    if max_depth[0] < depth:
        max_depth[0] = depth

    if root:
        for child in root.children:
            dfs(child, depth + 1, max_depth)
