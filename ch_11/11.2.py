# ALDS1_10_A: Fibonacci Number
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_10_A


def fib(n: int) -> int:
    if dp[n] is not None:
        return dp[n]
    else:
        if n in [0, 1]:
            dp[n] = 1
        else:
            dp[n] = fib(n=n-1) + fib(n=n-2)
        return dp[n]


def main() -> None:
    global dp
    dp = [None] * 50

    n = int(input())

    print('{}'.format(fib(n=n)))
    return None


if __name__ == '__main__':
    main()
