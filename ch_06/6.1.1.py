def factorial(n:int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n=n-1)


def main():
    n = int(input())
    print(factorial(n=n))


if __name__ == '__main__':
    main()
