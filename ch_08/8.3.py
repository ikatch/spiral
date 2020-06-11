# ALDS1_7_B: Binary Trees
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_7_B


class Node:
    def __init__(self, node_id: int = None, parent_id: int = -1, sibling_id: int = -1,
                 left_child_id: int = -1, right_child_id: int = -1, degree: int = 0,
                 depth: int = 0, height: int = 0, node_type: str = None) -> None:
        self.node_id = node_id
        self.parent_id = parent_id
        self.sibling_id = sibling_id
        self.left_child_id = left_child_id
        self.right_child_id = right_child_id
        self.degree = degree
        self.depth = depth
        self.height = height
        self.node_type = node_type


def get_depth(node_id: int = 0, depth: int = 0) -> None:
    nodes[node_id].depth = depth

    left_child_id = nodes[node_id].left_child_id
    right_child_id = nodes[node_id].right_child_id

    if left_child_id == -1:
        pass
    else:
        get_depth(node_id=left_child_id, depth=depth+1)

    if right_child_id == -1:
        pass
    else:
        get_depth(node_id=right_child_id, depth=depth+1)

    return None


def get_height(node_id: int = 0) -> int:
    left_child_id = nodes[node_id].left_child_id
    right_child_id = nodes[node_id].right_child_id
    
    if left_child_id == -1:
        left_height = 0
    else:
        left_height = get_height(node_id=left_child_id)

    if right_child_id == -1:
        right_height = 0
    else:
        right_height = get_height(node_id=right_child_id)

    height = max(left_height, right_height)
    nodes[node_id].height = height
    return height + 1


def get_type(degree: int, depth: int) -> str:
    if depth == 0:
        return 'root'
    elif degree > 0:
        return 'internal node'
    else:
        return 'leaf'


def main() -> None:
    n = int(input())

    global nodes
    nodes = []

    for node_id in range(n):
        node = Node(node_id=node_id)
        nodes.append(node)

    for _ in range(n):  # set left / right_child_id / parent_id / sibling_id
        val = list(map(int, input().split()))
        node_id = val[0]
        left_child_id = val[1]
        right_child_id = val[2]

        nodes[node_id].left_child_id = left_child_id
        nodes[node_id].right_child_id = right_child_id

        if left_child_id == -1:
            pass
        else:
            nodes[left_child_id].parent_id = node_id
            nodes[left_child_id].sibling_id = right_child_id
        if right_child_id == -1:
            pass
        else:
            nodes[right_child_id].parent_id = node_id
            nodes[right_child_id].sibling_id = left_child_id

    for node in nodes:  # get depth / height
        if node.parent_id == -1:  # i.e. root
            get_depth(node_id=node.node_id, depth=0)
            get_height(node_id=node.node_id)
            break
        else:
            pass

    for node in nodes:  # get degree / node_type
        node.degree = (node.left_child_id >= 0) + (node.right_child_id >= 0)
        node.node_type = get_type(degree=node.degree, depth=node.depth)

    for node in nodes:
        print('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.format(
            node.node_id, node.parent_id, node.sibling_id, node.degree, node.depth, node.height, node.node_type))

    return None


if __name__ == '__main__':
    main()
