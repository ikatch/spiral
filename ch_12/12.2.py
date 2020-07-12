# ALDS1_11_A: Graph
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_11_A


def main() -> None:
    n = int(input())

    M = []
    for _ in range(n):
        M.append([0] * n)

    for _ in range(n):
        cmd = list(map(int, input().split()))
        u, k, V = cmd[0], cmd[1], cmd[2:]
        for v in V:
            M[u-1][v-1] = 1

    for i in range(n):
        print(*M[i])

    return None


if __name__ == '__main__':
    main()
