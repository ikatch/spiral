# ALDS1_8_C: Binary Search Tree III
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_8_C


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

    def find(self, key: int, target: Node = None) -> Node:
        if target is None:
            target = self.root  # default value: root
        else:
            pass
        if target in self.nodes:
            while target is not None:  # find node whose key is key
                if target.key == key:
                    return target
                elif key < target.key:
                    target = target.left
                else:
                    target = target.right
            return None
        else:
            raise Exception('target does not exist')

    def get_min(self, target: Node = None) -> Node:
        while target.left is not None:
            target = target.left
        return target

    def get_successor(self, target: Node = None) -> Node:
        if target.right is not None:
            return self.get_min(target=target.right)
        else:
            parent = target.parent
            while parent is not None and target is parent.right:  # find the node who is the parent's left child
                target = parent
                parent = parent.parent
            return parent

    def delete(self, key: int, target: Node = None) -> None:
        target = self.find(key=key, target=target)
        # select node to remove (target itself or targets successor)
        if target.left is None or target.right is None:  # case 1: no child / case 2: one child
            node_remove = target
        else:  # two children
            node_remove = self.get_successor(target=target)  # case 3: two children
        # find child of node to remove
        if node_remove.left is not None:  # case 1: child is None
            child = node_remove.left      # case 2: child is target's left / right of target
        else:                             # case 3: child is successor's right (successor does not have left)
            child = node_remove.right
        # update parent of child
        if child is None:  # i.e. case 1
            pass
        else:  # i.e. case 2 / 3
            child.parent = node_remove.parent
        # update child of parent (current child of parent is node to remove)
        if node_remove.parent is None:  # i.e. node_remove is root
            self.root = child
        elif node_remove == node_remove.parent.left:  # check which child of parent is node to remove
            node_remove.parent.left = child
        else:
            node_remove.parent.right = child
        # case 3: update key of target with one of node to remove
        if node_remove == target:  # i.e. case 1 / 2
            pass
        else:  # i.e. case 3
            target.key = node_remove.key
        # remove from tree
        self.nodes.remove(node_remove)
        return None


def main() -> None:
    n = int(input())
    tree = BinarySearchTree()
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'insert':
            key = int(cmd[1])
            tree.insert(key=key)
        elif cmd[0] == 'find':
            key = int(cmd[1])
            if tree.find(key=key) is not None:
                print('yes')
            else:
                print('no')
        elif cmd[0] == 'delete':
            key = int(cmd[1])
            tree.delete(key=key)
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
