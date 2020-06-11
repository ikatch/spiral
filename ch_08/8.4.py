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


def preorder(node_id: int = -1) -> None:
    if node_id == -1:
        return None
    else:
        print(' {}'.format(node_id), end='')
        preorder(node_id=nodes[node_id].left_child_id)
        preorder(node_id=nodes[node_id].right_child_id)
    return None


def inorder(node_id: int = -1) -> None:
    if node_id == -1:
        return None
    else:
        inorder(node_id=nodes[node_id].left_child_id)
        print(' {}'.format(node_id), end='')
        inorder(node_id=nodes[node_id].right_child_id)
    return None


def postorder(node_id: int = -1) -> None:
    if node_id == -1:
        return None
    else:
        postorder(node_id=nodes[node_id].left_child_id)
        postorder(node_id=nodes[node_id].right_child_id)
        print(' {}'.format(node_id), end='')
    return None


def parse(node_id: int = -1, order: str = None) -> None:
    if node_id == -1:
        return None
    else:
        if order == 'preorder':
            preorder(node_id=node_id)
        elif order == 'inorder':
            inorder(node_id=node_id)
        elif order == 'postorder':
            postorder(node_id=node_id)
        else:
            return None
        print()
    return None


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
            parse(node_id=node.node_id, order='preorder')
            print('Inorder')
            parse(node_id=node.node_id, order='inorder')
            print('Postorder')
            parse(node_id=node.node_id, order='postorder')
            break
        else:
            pass

    return None


if __name__ == '__main__':
    main()
