# ALDS1_10_B: Matrix Chain Multiplication
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_10_B


def main() -> None:
    n = int(input())

    p = [None] * (n+1)
    for i in range(n):
        p[i], p[i+1] = list(map(int, input().split()))

    m = []

    for _ in range(n):
        m.append([None] * n)

    for i in range(0, n, 1):
        m[i][i] = 0

    for l in range(1, n, 1):
        for i in range(0, n-l, 1):
            j = i + l
            m[i][j] = 1 << 21
            for k in range(i, j, 1):  # find min m[i][j]
                m[i][j] = min(m[i][j], m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j])

    print(m[0][n-1])
    return None


if __name__ == '__main__':
    main()
