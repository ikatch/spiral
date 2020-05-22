import bisect


def main():
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))
    C = 0

    for t in T:
        idx = bisect.bisect_left(a=S, x=t)
        if idx < len(S) and S[idx] == t:
            C += 1

    print(C)


if __name__ == '__main__':
    main()
