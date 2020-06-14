
def print_set(S: set) -> None:
    print('{}: '.format(S.__len__()), end='')
    print(*sorted(S))  # set is not sorted automatically
    return None


def main() -> None:
    S = set()

    S.add(8)
    S.add(1)
    S.add(7)
    S.add(4)
    S.add(8)
    S.add(4)

    print_set(S=S)  # set is not sorted

    S.remove(7)

    print_set(S=S)

    S.add(2)

    print_set(S=S)

    if 10 in S:
        print('found.')
    else:
        print('not found.')
    return None


if __name__ == '__main__':
    main()
