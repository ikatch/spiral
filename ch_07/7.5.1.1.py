

def main() -> None:
    n = int(input())
    v = list(map(int, input().split()))

    v.sort()

    print(*v)

    return None


if __name__ == '__main__':
    main()
