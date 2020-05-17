# ALDS1_3_B: Queue
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_B


class Info:
    def __init__(self, name, time):
        self.name = name
        self.time = time


class Queue:
    def __init__(self, size):
        self.tail = 0
        self.head = 0
        self.size = size
        self.queue = [None] * self.size

    def is_empty(self) -> bool:
        return self.head == self.tail

    def is_full(self) -> bool:
        return self.head == self.tail % self.size and not self.is_empty()

    def enqueue(self, x):
        if self.is_full():
            raise Exception('Error: overflow')
        else:
            self.queue[self.tail % self.size] = x
            self.tail += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Error: underflow')
        else:
            x = self.queue[self.head % self.size]
            self.head += 1
            return x


def main():
    n, q = map(int, input().split())
    t = 0

    Q = Queue(size=n)

    for _ in range(0, n, 1):
        name, time = input().split()
        time = int(time)
        Q.enqueue(Info(name=name, time=time))

    while not Q.is_empty():
        i = Q.dequeue()
        c = min(q, i.time)
        i.time -= c
        t += c
        if i.time > 0:
            Q.enqueue(x=i)
        else:
            print('{} {}'.format(i.name, t))


if __name__ == '__main__':
    main()
