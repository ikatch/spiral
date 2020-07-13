# ALDS1_11_C: Breadth First Search
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_11_C
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
        self.discover_time = INFTY
        self.finish_time = None


class graph:
    def __init__(self):
        self.vertexes = []
        self.time = 0

    def add_vertex(self, id: int, edge: list) -> None:
        new_vertex = vertex(id=id, edge=edge)
        self.vertexes.append(new_vertex)

    def bfs(self, s: vertex) -> None:
        Q = deque([])

        Q.append(s)
        s.discover_time = 0

        while Q.__len__() > 0:
            u = Q.popleft()
            u.color = GRAY

            for e in u.edge:
                v = self.vertexes[e-1]
                if v.color == WHITE:
                    v.discover_time = u.discover_time + 1
                    v.color = GRAY
                    Q.append(v)

            u.color = BLACK

        for v in self.vertexes:
            print('{} {}'.format(v.id, v.discover_time if v.discover_time != INFTY else -1))
        return None


def main() -> None:
    n = int(input())

    G = graph()

    for _ in range(n):
        cmd = list(map(int, input().split()))
        id, __, edge = cmd[0], cmd[1], cmd[2:]
        G.add_vertex(id=id, edge=edge)

    G.bfs(s=G.vertexes[0])

    return None


if __name__ == '__main__':
    main()
