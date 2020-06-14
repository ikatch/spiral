# ALDS1_8_A: Binary Search Tree I
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_8_A


class Node:
    def __init__(self, key: int, parent=None, left=None, right=None) -> None:
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class BinaryTree:
    nodes = []
    root = None

    def __init__(self) -> None:
        pass

    def pre_order(self, target: Node, order=None) -> None:
        if order is None:
            order = []
        else:
            pass
        if target is None:
            return order
        else:
            order.append(target.key)
            self.pre_order(target=target.left, order=order)
            self.pre_order(target=target.right, order=order)
        return order

    def in_order(self, target: Node, order=None) -> None:
        if order is None:
            order = []
        else:
            pass
        if target is None:
            return order
        else:
            self.in_order(target=target.left, order=order)
            order.append(target.key)
            self.in_order(target=target.right, order=order)
        return order

    def post_order(self, target: Node, order=None) -> None:
        if order is None:
            order = []
        else:
            pass
        if target is None:
            return order
        else:
            self.post_order(target=target.left, order=order)
            self.post_order(target=target.right, order=order)
            order.append(target.key)
        return order


class BinarySearchTree(BinaryTree):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, key: int, target: Node = None) -> None:
        if target is None:
            if self.nodes.__len__() == 0:  # i.e. root
                node = Node(key=key)
                self.nodes.append(node)
                self.root = node
                return None
            else:
                target = self.root  # default value: root
        else:
            pass
        if target in self.nodes:
            while target is not None:  # find node where to insert
                if key < target.key:
                    if target.left is not None:
                        target = target.left
                    else:
                        break
                else:
                    if target.right is not None:
                        target = target.right
                    else:
                        break
            node = Node(key=key, parent=target)
            self.nodes.append(node)

            if key < target.key:
                target.left = node
            else:
                target.right = node
        else:
            raise Exception('target does not exist')
        return None


def main() -> None:
    n = int(input())
    tree = BinarySearchTree()
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'insert':
            key = int(cmd[1])
            tree.insert(key=key)
        elif cmd[0] == 'print':
            print(' ', end='')
            print(*tree.in_order(target=tree.root))
            print(' ', end='')
            print(*tree.pre_order(target=tree.root))
        else:
            raise Exception('Un-known command')
    return None


if __name__ == '__main__':
    main()
