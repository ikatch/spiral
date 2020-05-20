# ALDS1_1_D: Maximum Profit
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_D


def maximum_profit(n, R):
    max_profit = -2 * pow(10, 9)  # should be < 1 - pow(10, 9), minimum profit
    min_rate = R[0]

    for r in R[1:]:
        max_profit = max(max_profit, r - min_rate)
        min_rate = min(min_rate, r)

    return max_profit


def main():
    n = int(input())
    R = [int(input()) for _ in range(0, n, 1)]

    print(maximum_profit(n=n, R=R))


if __name__ == '__main__':
    main()