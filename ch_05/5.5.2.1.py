import bisect


def main() -> None:
    A: list = [1, 1, 2, 2, 2, 4, 5, 5, 6, 8, 8, 8, 10, 15]

    idx = bisect.bisect_left(a=A, x=3)
    print('A[{}] = {}'.format(idx, A[idx]))

    idx = bisect.bisect_left(a=A, x=2)
    print('A[{}] = {}'.format(idx, A[idx]))


if __name__ == '__main__':
    main()
