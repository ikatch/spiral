# ALDS1_3_D: Areas on the Cross-Section Diagram
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_3_D

def main():
    cmd = list(input())
    S1 = []
    S2 = []
    sum = 0

    # total area
    for i in range(len(cmd)):
        if cmd[i] == '\\':
            S1.append(i)
        elif cmd[i] == '/' and len(S1) > 0:
            j = S1.pop()
            sum += i - j

            a = i - j
            while len(S2) > 0 and S2[-1][0] > j:
                a += S2[-1][1]
                S2.pop()

            S2.append([j, a])
    print(sum)

    # each area
    ans = []
    while len(S2) > 0:
        ans.append(S2[-1][1])
        S2.pop()
    ans.reverse()

    n = len(ans)
    if n == 0:
        print(n)
    if n > 0:
        print(n, end=' ')
        print(*ans)


if __name__ == '__main__':
    main()
