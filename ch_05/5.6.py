# ALDS1_4_D: Allocation
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_4_D
import math

MIN_P = 0
MAX_P = 100000 * 10000


def check(w:list, k:int, P:int) -> int:
    i = 0
    for _ in range(k):
        q = 0
        while i < len(w) and q + w[i] <= P:
            q += w[i]
            i += 1
    return i


def solve(w:list, k:int) -> int:
    left = MIN_P
    right = MAX_P

    while right - left > 1:
        P = math.ceil((left + right) / 2)
        i = check(w=w, k=k, P=P)
        if i < len(w):
            left = P
        else:
            right = P

    P = right

    return P


def main():
    n, k = list(map(int, input().split()))
    w = [int(input()) for _ in range(n)]
    ans = solve(w=w, k=k)
    print(ans)


if __name__ == '__main__':
    main()
