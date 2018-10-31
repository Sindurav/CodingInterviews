# Time Complexity - O(n)
# Space Complexity - O(1) if we are ignoring the call stack of recursion
# Space Complexity - O(n) if we are considering the call stack of recursion


class Node(object):
    def __init__(self, value):
        self.value = value
        # self.left = None
        # self.right = None
        self.child = [None, None]


class Tree(object):
    def __init__(self, value):
        self.root = Node(value)

    def insert_node(self, value, node):

        if value > node.value:
            if node.child[1]:
                self.insert_node(value, node.child[1])
            else:
                node.child[1] = Node(value)
        else:
            if node.child[0]:
                self.insert_node(value, node.child[0])
            else:
                node.child[0] = Node(value)


def validate_binary_tree(node):
    flag = [True]
    return recurse(node, -float("inf"), float("inf"), flag)


def recurse(node, min_val, max_val, flag):
    if not flag[0]:
        return False

    if not node:
        return True

    if len(node.child) > 2:
        flag[0] = False
        return False

    if min_val < node.value < max_val:
        return recurse(node.child[0], min_val, node.value, flag) and recurse(node.child[1], node.value, max_val, flag)
    else:
        flag[0] = False
        return False


tree = Tree(5)
tree.insert_node(1, tree.root)
tree.insert_node(2, tree.root)
tree.insert_node(6, tree.root)
tree.insert_node(7, tree.root)

not_bin_tree = Node(5)
not_bin_tree.child[0] = Node(3)
not_bin_tree.child[1] = Node(7)
not_bin_tree.child.append(Node(9))

#     5
#   /   \
#  6     7

is_binary_tree = validate_binary_tree(None)
print(is_binary_tree)

is_binary_tree = validate_binary_tree(not_bin_tree)
print(is_binary_tree)
