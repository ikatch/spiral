# ALDS1_3_A: Stack
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_A


def main():
    A = list(input().split())
    s = []

    for a in A:
        if a in ['+', '-', '*']:
            num1 = s.pop()
            num0 = s.pop()

            if a == '+':
                s.append(num0+num1)
            elif a == '-':
                s.append(num0-num1)
            else:
                s.append(num0*num1)
        else:
            s.append(int(a))
    print(s.pop())


if __name__ == '__main__':
    main()
