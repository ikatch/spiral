# ALDS1_5_B: Merge SortKoch Curve
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_5_B
import math

MAX = 5 * 10 ** 5
SENTINEL = 2 * 10 ** 9


def merge(A: list, left: int, mid: int, right: int, cnt: int) -> (list, int):
    L = A[left:mid]
    R = A[mid:right]

    L.append(SENTINEL)
    R.append(SENTINEL)

    i = 0
    j = 0

    for k in range(left, right, 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    cnt += right - left
    return A, cnt


def merge_sort(A: list, left: int, right: int, cnt: int) -> (list, int):
    if left + 1 < right:
        mid = math.ceil((left + right) / 2)
        A, cnt = merge_sort(A=A, left=left, right=mid, cnt=cnt)
        A, cnt = merge_sort(A=A, left=mid, right=right, cnt=cnt)
        A, cnt = merge(A=A, left=left, mid=mid, right=right, cnt=cnt)
    else:
        pass
    return A, cnt


def main() -> None:
    n = int(input())
    S = list(map(int, input().split()))
    cnt = 0

    S, cnt = merge_sort(A=S, left=0, right=len(S), cnt=cnt)

    print(*S)
    print(cnt)

    return None


if __name__ == '__main__':
    main()
