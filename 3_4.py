# ALDS1_2_B: Selection Sort
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_B


def selection_sort(A:list) -> (list, int):
    N:int = len(A)
    sw: int = 0

    for i in range(0, N, 1):
        min_j = i
        for j in range(i, N, 1):
            if A[j] < A[min_j]:
                min_j = j

        if i != min_j:
            A[i], A[min_j] = A[min_j], A[i]
            sw += 1

    return A, sw


def trace(A:list) -> None:
    for a in A[:-1]:
        print(a, end=' ')

    print(A[-1])


def main():
    N: int = int(input())
    A: list = list(map(int, input().split()))

    A, sw = selection_sort(A=A)

    trace(A=A)
    print(sw)


if __name__ == '__main__':
    main()
