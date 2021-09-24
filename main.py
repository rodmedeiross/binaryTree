import collections

class TreeNode:

    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        str = self.key
        if(self.left is not None):
            str += '[' + self.left.key + ']'
        if(self.right is not None):
            str += '[' + self.right.key + ']'
        return str


def is_leaf(tree_node):
    return tree_node == None or (tree_node.left == None and tree_node.right == None)

def generate_tree(edges):
    children = collections.defaultdict(set)
    nodes = set()
    for u, v in edges:
        children[u].add(v)
        nodes.add(u)
        nodes.add(v)

    def dfs(start, target):
        if start == target:
            return True
        result = False
        for next_node in children[start]:
            # in case we have edge that points to a node itself
            if next_node != start:
                result = result or dfs(next_node, target)
        return result

    for node in nodes:
        for child in list(children[node]):
            found = False
            for other_child in list(children[node]):
                if other_child != child and dfs(other_child, child):
                    found = True
                    break
            if found:
                raise Exception('ERRO')
                # children[node].remove(child)

    return children

def count_depth(tree_node):
    if(tree_node is None):
        return 0

    count = 1
    count += count_depth(tree_node.left)
    count += count_depth(tree_node.right)

    return count


def build_tree(edges):
    tree_dict = generate_tree(edges)
    tree_dict_cpy = generate_tree(edges)
    if(tree_dict is None):
        return

    nodes = []
    node_keys = []

    keys_iter = iter(reversed(tree_dict.keys()))
    values_iter = iter(reversed(tree_dict.values()))
    next_key = next(keys_iter)
    next_value = next(values_iter)

    while(next_key is not None):
        left = None
        if(len(next_value) > 0):
            left_key = next_value.pop()
            if(node_keys.__contains__(left_key)):
                left = nodes[node_keys.index(left_key)]
        right = None
        if(len(next_value) > 0):
            right_key = next_value.pop()
            if(node_keys.__contains__(right_key)):
                right = nodes[node_keys.index(right_key)]
        node = TreeNode(next_key, left, right)
        if(node_keys.__contains__(node.key) == False):
            nodes.append(node)
            node_keys.append(node.key)
        next_key = next(keys_iter, None)
        next_value = next(values_iter, None)

    keys_iter = iter(reversed(tree_dict_cpy.keys()))
    values_iter = iter(reversed(tree_dict_cpy.values()))
    next_key = next(keys_iter)
    next_value = next(values_iter)

    while(next_key is not None):
        left = None
        if(len(next_value) > 0):
            left_key = next_value.pop()
            if(node_keys.__contains__(left_key)):
                left = nodes[node_keys.index(left_key)]
        right = None
        if(len(next_value) > 0):
            right_key = next_value.pop()
            if(node_keys.__contains__(right_key)):
                right = nodes[node_keys.index(right_key)]
        if(node_keys.__contains__(next_key) == False):
            nodes.append(TreeNode(next_key, left, right))
            node_keys.append(next_key)
        else:
            node = nodes[node_keys.index(next_key)]
            node.left = left
            node.right = right
        next_key = next(keys_iter, None)
        next_value = next(values_iter, None)

    max_count_node = 0
    max_count_node_index = 0
    for i in nodes:
        count = count_depth(i)
        if(count > max_count_node):
            max_count_node = count
            max_count_node_index = nodes.index(i)


    return nodes[max_count_node_index]

def print_tree_sub(tree_node):
    if(tree_node is None):
        return ''

    str = ''
    if(is_leaf(tree_node)):
        str += '['
        str += tree_node.key
        str += ']'
    else:
        str += tree_node.key

        if(is_leaf(tree_node.left) and is_leaf(tree_node.right)):
            str += print_tree_sub(tree_node.left)
            str += print_tree_sub(tree_node.right)
        else:
            if(is_leaf(tree_node.left) == False):
                str += '['
            str += print_tree_sub(tree_node.left)
            if(is_leaf(tree_node.left) == False):
                str += ']'

            if(is_leaf(tree_node.right) == False):
                str += '['
            str += print_tree_sub(tree_node.right)
            if(is_leaf(tree_node.right) == False):
                str += ']'

    return str

def print_tree_root(tree_node):
    if(tree_node is None):
        return

    str = tree_node.key

    if(is_leaf(tree_node) == False):
        str += '['
        str += '\n'

        if(tree_node.left is not None):
            str += '['
            str += print_tree_sub(tree_node.left)
            str += ']'

        str += '\n'

        if(tree_node.right is not None):
            str += '['
            str += print_tree_sub(tree_node.right)
            str += ']'

        str += '\n'
        str += ']'

    return str

# Example 1 [A,B] [A,C] [B,G] [C,H] [E,F] [B,D] [C,E]
print(
    print_tree_root(
        build_tree(
            [('A', 'B'), ('A', 'C'), ('B', 'G'), ('C', 'H'), ('E', 'F'), ('B', 'D'), ('C', 'E')]
        )
    )
)
#
# # Example 2 [B,D] [D,E] [A,B] [C,F] [E,G] [A,C]
print(
    print_tree_root(
        build_tree(
            [('B', 'D'), ('D', 'E'), ('A', 'B'), ('C', 'F'), ('E', 'G'), ('A', 'C')]
        )
    )
)

# Example 3 [A,B] [A,C] [B,D] [D,C]
print(
    print_tree_root(
        build_tree(
            [('A', 'B'), ('A', 'C'), ('B', 'D'), ('D', 'C')]
        )
    )
)
