# ALDS1_11_D: Connected Components
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_11_D
from collections import deque

WHITE = 0
GRAY = 1
BLACK = 2

INFTY = 1 << 21


class vertex:
    def __init__(self, id: int, edge: list):
        self.id = id
        self.edge = edge
        self.color = WHITE
        self.discover_time = None
        self.finish_time = None
        self.label = None


class graph:
    def __init__(self):
        self.vertexes = []
        self.time = 0

    def add_vertex(self, id: int, edge: list) -> None:
        new_vertex = vertex(id=id, edge=edge)
        self.vertexes.append(new_vertex)

    def bfs(self, s: vertex, label: int) -> None:
        if s.label is not None:
            return None
        else:
            Q = deque([])

            Q.append(s)

            while Q.__len__() > 0:
                u = Q.popleft()
                u.color = GRAY

                for e in u.edge:
                    v = self.vertexes[e]
                    if v.color == WHITE:
                        v.color = GRAY
                        Q.append(v)

                u.color = BLACK
                u.label = label
        return None


def main() -> None:
    n, m = list(map(int, input().split()))

    G = graph()

    for id in range(n):
        G.add_vertex(id=id, edge=[])

    for _ in range(m):
        i, j = list(map(int, input().split()))
        G.vertexes[i].edge.append(j)
        G.vertexes[j].edge.append(i)

    for v in G.vertexes:
        G.bfs(s=v, label=v.id)

    q = int(input())

    for _ in range(q):
        i, j = list(map(int, input().split()))
        print('yes' if G.vertexes[i].label is G.vertexes[j].label else 'no')

    return None


if __name__ == '__main__':
    main()
