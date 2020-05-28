# ALDS1_6_D: Minimum Cost Sort
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_6_D
import copy


def min_sort_cost(W: list) -> int:
    num = len(W)
    min_w = min(W)

    c = 0  # sorting cost

    X = copy.deepcopy(W)
    X.sort()  # result W sorted

    L = [None] * (max(W) + 1)
    for i in range(num):
        L[X[i]] = i  # location id of W[-] members after sorting

    B = [False] * num  # Flag list to show whether W[-] belongs to any cycle or not

    for i in range(num):  # loop to explore cycles and each cost
        if B[i]:  # check whether already belongs to any cycle or not
            continue
        else:  # start to explore a cycle
            cur = i  # location of current target weight member in W
            cycle = []  # cycle members

            while True:  # loop to explore cycle members
                w = W[cur]  # current target weight member
                cycle.append(w)  # add to cycle
                B[cur] = True  # raise flag to show that w has a cycle to belong
                cur = L[w]  # update to next weight members in a cycle

                if B[cur]:  # made cycle or not
                    break
                else:
                    continue
            # calculate cost
            sigma_w_i = sum(cycle)
            min_w_i = min(cycle)
            n = len(cycle)

            c += min(sigma_w_i + (n - 2) * min_w_i, sigma_w_i + min_w_i + (n + 1) * min_w)
    return c


def main() -> None:
    _ = int(input())
    W = list(map(int, input().split()))

    c = min_sort_cost(W=W)
    print(c)

    return None


if __name__ == '__main__':
    main()
