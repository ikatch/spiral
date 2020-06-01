# ALDS1_7_A: Rooted Trees
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_7_A
from functools import lru_cache


class Node:
    def __init__(self, parent: int = None, left: int = None, right: int = None) -> None:
        self.parent = parent
        self.left = left
        self.right = right

        return None


@lru_cache(maxsize=1000)
def get_depth(T: list, D: list, u: int, depth: int) -> (list, list):
    D[u] = depth
    if T[u].right is not None:
        T, D = get_depth(T=T, D=D, u=T[u].right, depth=depth)
    else:
        pass

    if T[u].left is not None:
        T, D = get_depth(T=T, D=D, u=T[u].left, depth=depth + 1)
    else:
        pass

    return T, D


def get_child(T: list, u: int) -> list:
    children = []
    child = T[u].left

    while child is not None:
        children.append(child)
        child = T[child].right

    return children


def get_type(depth: int, children: list) -> str:
    if depth == 0:
        return 'root'
    elif len(children) > 0:
        return 'internal node'
    else:
        return 'leaf'


def main() -> None:
    n = int(input())

    T = []
    D = [None] * n
    C = []
    types = []

    for _ in range(n):
        T.append(Node())

    for _ in range(n):
        info = list(map(int, input().split()))

        u = info[0]  # target node number
        children = info[2:]

        for c in children:  # children of T[u]
            if children.index(c) == 0:  # left-most child
                T[u].left = c
            else:  # another child
                T[l].right = c  # brother of left one
            l = c
            T[c].parent = u

    for u in T:
        if u.parent is None:  # i.e. root
            r = T.index(u)
            u.parent = -1

    T, D = get_depth(T=T, D=D, u=r, depth=0)

    for i in range(n):
        C.append(get_child(T=T, u=i))
        types.append(get_type(depth=D[i], children=C[i]))

    for i in range(n):
        print('node {}: parent = {}, depth = {}, {}, {}'.format(i, T[i].parent, D[i], types[i], C[i]))

    return None


if __name__ == '__main__':
    main()
