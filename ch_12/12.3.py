# ALDS1_11_B: Depth First Search
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_11_B
WHITE = 0
GRAY = 1
BLACK = 2


def dfs_visit(u: int) -> None:
    global tt
    color[u] = GRAY
    tt += 1
    d[u] = tt
    for v in range(n):
        if M[u][v] == 0:
            continue
        if color[v] == WHITE:
            dfs_visit(u=v)
    color[u] = BLACK
    tt += 1
    f[u] = tt

    return None


def dfs() -> None:
    global tt
    for u in range(n):
        color[u] = WHITE
    tt = 0

    for u in range(n):
        if color[u] == WHITE:
            dfs_visit(u=u)
    for u in range(n):
        print('{} {} {}'.format(u + 1, d[u], f[u]))
    return None


def main() -> None:
    global n
    n = int(input())

    global M
    global color
    global d
    global f
    global tt

    M = []
    for _ in range(n):
        M.append([0] * n)

    color = [None] * n
    d = [None] * n
    f = [None] * n

    for _ in range(n):
        cmd = list(map(int, input().split()))
        u, k, V = cmd[0], cmd[1], cmd[2:]
        for v in V:
            M[u - 1][v - 1] = 1

    dfs()

    return None


if __name__ == '__main__':
    main()
