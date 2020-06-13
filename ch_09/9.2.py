# ALDS1_8_A: Binary Search Tree 1
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_8_A


class Node:
    def __init__(self, key: int, parent=None, left=None, right=None) -> None:
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def insert(self, target) -> None:
        if target is None:  # i.e. root of tree
            pass
        else:
            while target is not None:  # find node where to insert
                if self.key < target.key:
                    if target.left is not None:
                        target = target.left
                    else:
                        break
                else:
                    if target.right is not None:
                        target = target.right
                    else:
                        break

            self.parent = target
            if self.key < target.key:
                target.left = self
            else:
                target.right = self
        return None


def pre_order(target: Node, order=None) -> None:
    if order is None:
        order = []
    else:
        pass

    if target is None:
        return order
    else:
        order.append(target.key)
        pre_order(target=target.left, order=order)
        pre_order(target=target.right, order=order)
    return order


def in_order(target: Node, order=None) -> None:
    if order is None:
        order = []
    else:
        pass

    if target is None:
        return order
    else:
        in_order(target=target.left, order=order)
        order.append(target.key)
        in_order(target=target.right, order=order)
    return order


def post_order(target: Node, order=None) -> None:
    if order is None:
        order = []
    else:
        pass

    if target is None:
        return order
    else:
        post_order(target=target.left, order=order)
        post_order(target=target.right, order=order)
        order.append(target.key)
    return order


def main() -> None:
    n = int(input())
    tree = None
    root = None

    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'insert':
            key = int(cmd[1])
            if tree is None:
                tree = [Node(key=key)]
                root = tree[0]
            else:
                tree.append(Node(key=key))
                tree[-1].insert(target=root)
        elif cmd[0] == 'print':
            print(' ', end='')
            print(*in_order(target=root))
            print(' ', end='')
            print(*pre_order(target=root))
        else:
            raise Exception('Un-known command')

    return None


if __name__ == '__main__':
    main()
