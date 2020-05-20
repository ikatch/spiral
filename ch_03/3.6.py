# ALDS1_2_D: Shell Sort
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_2_D


def insertion_sort(A:list, g:int, cnt:int) -> (list, int):
    for i in range(g, len(A), 1):
        v = A[i]
        j = i - g

        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1

        A[j+g] = v
    return A, cnt


def shell_sort(A:list, n:int, cnt):
    G = []
    h = 1

    while h <= n:
        G.append(h)
        h = 3*h + 1

    G.reverse()

    for g in G:
        A, cnt = insertion_sort(A=A, g=g, cnt=cnt)

    return A, cnt, G


def main():
    n = int(input())
    A = [int(input()) for _ in range(0, n, 1)]

    cnt = 0

    A, cnt, G = shell_sort(A=A, n=n, cnt=cnt)

    print(len(G))
    print(*G)
    print(cnt)
    print(*A, sep='\n')


if __name__ == '__main__':
    main()
