# ALDS1_7_C: Tree Walk
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_7_C


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


def pre_order(node_id: int = -1, order=None) -> None:
    if order is None:
        order = []
    if node_id == -1:
        return order
    else:
        order.append(node_id)
        pre_order(node_id=nodes[node_id].left_child_id, order=order)
        pre_order(node_id=nodes[node_id].right_child_id, order=order)
    return order


def in_order(node_id: int = -1, order=None) -> None:
    if order is None:
        order = []
    if node_id == -1:
        return order
    else:
        in_order(node_id=nodes[node_id].left_child_id, order=order)
        order.append(node_id)
        in_order(node_id=nodes[node_id].right_child_id, order=order)
    return order


def post_order(node_id: int = -1, order=None) -> None:
    if order is None:
        order = []
    if node_id == -1:
        return order
    else:
        post_order(node_id=nodes[node_id].left_child_id, order=order)
        post_order(node_id=nodes[node_id].right_child_id, order=order)
        order.append(node_id)
    return order


def main() -> None:
    n = int(input())

    global nodes
    nodes = []

    for node_id in range(n):
        node = Node(node_id=node_id)
        nodes.append(node)

    for _ in range(n):  # set left / right_child_id / parent_id
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
        if right_child_id == -1:
            pass
        else:
            nodes[right_child_id].parent_id = node_id

    for node in nodes:
        if node.parent_id == -1:  # i.e. root
            print('Preorder')
            print(' ', end='')
            print(*pre_order(node_id=node.node_id))
            print('Inorder')
            print(' ', end='')
            print(*in_order(node_id=node.node_id))
            print('Postorder')
            print(' ', end='')
            print(*post_order(node_id=node.node_id))
            break
        else:
            pass

    return None


if __name__ == '__main__':
    main()
