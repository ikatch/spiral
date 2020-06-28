# ALDS1_10_C: Longest Common Subsequence
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_10_C


def lcs(X: str, Y: str) -> int:
    m = X.__len__()
    n = Y.__len__()

    c = []
    for _ in range(m+1):
        c.append([None] * (n+1))

    max_len = 0

    X = ' ' + X
    Y = ' ' + Y

    for i in range(m+1):
        c[i][0] = 0

    for j in range(n+1):
        c[0][j] = 0

    for i in range(1, m+1, 1):
        for j in range(1, n+1, 1):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])

    for i in range(m+1):
        max_len = max(max_len, max(c[i]))

    return max_len


def main() -> None:
    n = int(input())

        s1 = input()
        s2 = input()

        print(lcs(X=s1, Y=s2))

    return None


if __name__ == '__main__':
    main()
