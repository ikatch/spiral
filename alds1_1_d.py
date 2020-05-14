def main():
    n = int(input())
    R = [int(input()) for _ in range(0, n, 1)]

    max_v = -2 * 10 ^ 9
    min_v = R[0]

    for r in R[1:]:
        max_v = max(max_v, r - min_v)
        min_v = min(min_v, r)

    print(max_v)


if __name__ == "__main__":
    main()
