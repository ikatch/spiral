# ALDS1_3_C: Doubly Linked List
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_B
from collections import deque


def main():
    n = int(input())
    dli = deque()

    for _ in range(0, n, 1):
        cmd = input()

        if cmd == 'deleteFirst':
            dli.popleft()
        elif cmd == 'deleteLast':
            dli.pop()
        else:
            cmd, obj = cmd.split()
            if cmd == 'insert':
                dli.appendleft(obj)
            elif cmd == 'delete':
                try:
                    dli.remove(obj)
                except:
                    pass

    print(*dli)


if __name__ == '__main__':
    main()
