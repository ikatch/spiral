def print_list(x: list) -> None:
    for i in range(len(x)):
        print(x[i], end='')
    print()


def main() -> None:
    N: int = 4
    v: list = list(map(int, input().split()))

    print_list(x=v)

    i = 0
    v[i] = 3
    i += 1
    v[i] += 1

    print_list(x=v)


if __name__ == '__main__':
    main()
