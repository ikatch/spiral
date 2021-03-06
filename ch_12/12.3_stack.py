# ALDS1_11_B: Depth First Search
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_11_B
WHITE = 0
GRAY = 1
BLACK = 2


class vertex:
    def __init__(self, id: int, edge: list):
        self.id = id
        self.edge = edge
        self.color = WHITE
        self.discover_time = None
        self.finish_time = None


class graph:
    def __init__(self):
        self.vertexes = []
        self.time = 0

    def add_vertex(self, id: int, edge: list) -> None:
        new_vertex = vertex(id=id, edge=edge)
        self.vertexes.append(new_vertex)

    def dfs_visit(self, v: vertex) -> None:
        S = []
        focused_edge_num = [0] * self.vertexes.__len__()

        S.append(v)

        v.color = GRAY
        self.time += 1
        v.discover_time = self.time

        while S.__len__() > 0:
            w = S[-1]
            i = focused_edge_num[w.id-1]
            focused_edge_num[w.id-1] += 1

            if i < w.edge.__len__():
                x = self.vertexes[w.edge[i]-1]
                if x.color == WHITE:
                    x.color = GRAY
                    self.time += 1
                    x.discover_time = self.time

                    S.append(x)
                else:
                    pass
            else:
                S.pop()
                w.color = BLACK
                self.time += 1
                w.finish_time = self.time

        return None

    def dfs(self) -> None:
        self.time = 0

        for v in self.vertexes:
            if v.color == WHITE:
                self.dfs_visit(v=v)
        for v in self.vertexes:
            print('{} {} {}'.format(v.id, v.discover_time, v.finish_time))
        return None


def main() -> None:
    n = int(input())

    G = graph()

    for _ in range(n):
        cmd = list(map(int, input().split()))
        id, __, edge = cmd[0], cmd[1], cmd[2:]
        G.add_vertex(id=id, edge=edge)

    G.dfs()

    return None


if __name__ == '__main__':
    main()
