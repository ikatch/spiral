# ALDS1_9_A: Complete Binary Tree
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_9_A


def parent(id: int) -> int:
    return id // 2


def left(id: int) -> int:
    return 2 * id


def right(id: int) -> int:
    return 2 * id + 1


def main() -> None:
    H = int(input())
    A = list(map(int, input().split()))

    for id in range(1, H+1, 1):
        print('node {}: '.format(id), end='')
        print('key = {}, '.format(A[id-1]), end='')
        print('parent key = {}, '.format(A[parent(id=id)-1]), end='') if parent(id=id) >= 1 else None
        print('left key = {}, '.format(A[left(id=id)-1]), end='') if left(id=id) <= H else None
        print('right key = {}, '.format(A[right(id=id)-1]), end='') if right(id=id) <= H else None
        print()

    return None


if __name__ == '__main__':
    main()
