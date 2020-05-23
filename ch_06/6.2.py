# ALDS1_5_A: Exhausive Search
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_5_A
from functools import lru_cache


@lru_cache(maxsize=2 ** 12)  # memorization. if not used, to be TLE
def solve(i: int, m: int) -> bool:
    if m == 0:
        return True
    elif i >= n:
        return False
    else:
        return solve(i=i + 1, m=m) or solve(i=i + 1, m=m - A[i])


def main():
    global n
    global A

    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    M = list(map(int, input().split()))

    for m in M:
        # if solve(A=A, m=m):
        if solve(i=0, m=m):
            print('yes')
        else:
            print('no')


if __name__ == '__main__':
    main()
