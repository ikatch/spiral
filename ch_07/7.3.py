# ALDS1_6_C: Quick Sort
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_6_C
import copy
import math

MAX = 10 ** 5
SENTINEL = 2 * 10 ** 9


def merge(A: list, left: int, mid: int, right: int) -> list:
    L = A[left:mid]
    R = A[mid:right]

    L.append(['Z', SENTINEL])
    R.append(['Z', SENTINEL])

    i = 0
    j = 0

    for k in range(left, right, 1):
        if L[i][1] <= R[j][1]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A


def merge_sort(A: list, left: int, right: int) -> list:
    if left + 1 < right:
        mid = math.ceil((left + right) / 2)
        A = merge_sort(A=A, left=left, right=mid)
        A = merge_sort(A=A, left=mid, right=right)
        A = merge(A=A, left=left, mid=mid, right=right)
    else:
        pass
    return A


def partition(A: list, p: int, r: int) -> (list, int):
    x = A[r]

    i = p
    for j in range(p, r, 1):
        if A[j][1] <= x[1]:
            A[i], A[j] = A[j], A[i]
            i += 1
        else:
            pass
    A[i], A[r] = A[r], A[i]
    q = i
    return A, q


def quick_sort(A: list, p: int, r: int) -> list:
    if p < r:
        A, q = partition(A=A, p=p, r=r)
        A = quick_sort(A=A, p=p, r=q-1)
        A = quick_sort(A=A, p=q+1, r=r)
    else:
        pass
    return A


def main() -> None:
    n = int(input())
    S = [list(input().split()) for _ in range(n)]
    for s in S:
        s[1] = int(s[1])

    A = copy.deepcopy(S)
    B = copy.deepcopy(S)

    A = merge_sort(A=A, left=0, right=n)
    B = quick_sort(A=B, p=0, r=n-1)

    col_A = [a[0] for a in A]
    col_B = [b[0] for b in B]

    if col_A == col_B:
        print('Stable')
    else:
        print('Not stable')
    for b in B:
        print(*b)
    return None


if __name__ == '__main__':
    main()
