# ALDS1_7_A: Rooted Trees
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_7_A


class Node:
    def __init__(self, node_id: int = None, parent_id: int = -1, depth: int = 0, children_id: list = [],
                 node_type: str = None) -> None:
        self.node_id = node_id
        self.parent_id = parent_id
        self.depth = depth
        self.children_id = children_id
        self.node_type = node_type


def get_depth(node_id: int = 0, depth: int = 0) -> None:
    nodes[node_id].depth = depth
    for child_id in nodes[node_id].children_id:
        get_depth(node_id=child_id, depth=depth+1)
    return None


def get_type(depth: int, children_num: int) -> str:
    if depth == 0:
        return 'root'
    elif children_num > 0:
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

    for _ in range(n):  # set children_id
        val = list(map(int, input().split()))
        node_id = val[0]
        children_id = val[2:]
        nodes[node_id].children_id = children_id

    for node in nodes:  # set parent_id
        for child_id in node.children_id:
            nodes[child_id].parent_id = node.node_id

    for node in nodes:  # get depth
        if node.parent_id == -1:  # i.e. root
            get_depth(node_id=node.node_id, depth=0)
            break
        else:
            pass

    for node in nodes:  # get node_type
        node.node_type = get_type(depth=node.depth, children_num=len(node.children_id))

    for node in nodes:
        print('node {}: parent = {}, depth = {}, {}, {}'.format(node.node_id, node.parent_id, node.depth,
                                                                node.node_type, node.children_id))

    return None


if __name__ == '__main__':
    main()
