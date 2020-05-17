# ALDS1_2_A: Bubble Sort
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_A


def bubble_sort(A:list) -> (list, int):
    sw: int = 0
    flag: bool = True

    i: int = 0

    while flag:
        flag = False

        for j in reversed(range(i+1, len(A), 1)):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]

                flag = True
                sw += 1

        i += 1

    return A, sw


def trace(A:list) -> None:
    for a in A[:-1]:
        print(a, end=' ')

    print(A[-1])


def main():
    N: int = int(input())
    A: list = list(map(int, input().split()))

    A, sw = bubble_sort(A=A)

    trace(A=A)
    print(sw)


if __name__ == '__main__':
    main()
