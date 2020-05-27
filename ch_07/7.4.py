# ALDS1_6_A: Counting Sort
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_6_A


def counting_sort(A: list) -> list:
    n = len(A)
    B = [None] * n
    C = [0] * (max(A) + 1)

    for a in A:
        C[a] += 1
    for i in range(1, len(C), 1):
        C[i] += C[i-1]
    for a in A:
        B[C[a]-1] = a
        C[a] -= 1

    return B


def main() -> None:
    n = int(input())
    A = list(map(int, input().split()))

    A = counting_sort(A=A)

    print(*A)

    return None


if __name__ == '__main__':
    main()
