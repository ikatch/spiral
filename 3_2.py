# ALDS1_1_A: Insertion Sort
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_A


def trace(A:list):
    for a in A[:-1]:
        print(a, end=' ')

    print(A[-1])


def insertion_sort(A):
    trace(A)

    v = A[0]

    for i in range(1, len(A), 1):
        v = A[i]
        j = i - 1

        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = v

        trace(A)

    return A


def main():
    N = int(input())
    A = list(map(int, input().split()))

    A = insertion_sort(A=A)


if __name__ == '__main__':
    main()
