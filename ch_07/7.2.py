# ALDS1_6_B: Partition
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_6_B


def partition(A: list, p: int, r: int) -> (list, int):
    x = A[r]

    i = p
    for j in range(p, r, 1):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
        else:
            pass
    A[i], A[r] = A[r], A[i]
    q = i
    return A, q


def main() -> None:
    n = int(input())
    A = list(map(int, input().split()))
    r = n - 1

    A, q = partition(A=A, p=0, r=r)

    for i in range(0, n, 1):
        if i != q:
            print(A[i], end='')
        else:
            print('[{}]'.format(A[i]), end='')

        if i < n - 1:
            print(' ', end='')
        else:
            print()

    return None


if __name__ == '__main__':
    main()
