# ALDS1_3_B: Queue
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_B
from collections import deque


class Info:
    def __init__(self, name, time):
        self.name = name
        self.time = time


def main():
    n, q = map(int, input().split())
    t = 0

    Q = deque()

    for _ in range(0, n, 1):
        name, time = input().split()
        time = int(time)
        Q.append(Info(name=name, time=time))

    while len(Q) > 0:
        i = Q.popleft()
        c = min(q, i.time)
        i.time -= c
        t += c
        if i.time > 0:
            Q.append(i)
        else:
            print('{} {}'.format(i.name, t))


if __name__ == '__main__':
    main()
