# ALDS1_3_C: Doubly Linked List
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_B
from collections import deque


def main():
    n = int(input())
    dli = deque()

    for _ in range(0, n, 1):
        cmd = input()

        if cmd[0] == 'i':
            obj = int(cmd.split()[1])
            dli.appendleft(obj)
        elif cmd[6] == 'L':
            dli.pop()
        elif cmd[6] == 'F':
            dli.popleft()
        elif cmd[0] == 'd':
            obj = int(cmd.split()[1])
            try:
                dli.remove(obj)
            except:
                pass

    print(*dli)


if __name__ == '__main__':
    main()
