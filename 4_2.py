# ALDS1_3_A: Stack
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_A


class Stack:
    def __init__(self, size=1000):
        self.size = size
        self.stack = []
        self.top = 0

    def initialize(self):
        self.stack = []
        self.top = 0

    def is_empty(self) -> bool:
        return self.top == 0

    def is_full(self) -> bool:
        return self.top >= self.size - 1

    def push(self, x):
        if self.is_full():
            raise Exception('Error: stack overflow')
        else:
            self.top += 1
            self.stack.append(x)

    def pop(self):
        if self.is_empty():
            raise Exception('Error: stack underflow')
        else:
            self.top -= 1
            return self.stack.pop()


def main():
    A = list(input().split())
    s = Stack()

    for a in A:
        if a in ['+', '-', '*']:
            num1 = s.pop()
            num0 = s.pop()

            if a == '+':
                s.push(x=num0+num1)
            elif a == '-':
                s.push(x=num0-num1)
            else:
                s.push(x=num0*num1)
        else:
            s.push(int(a))
    print(s.pop())


if __name__ == '__main__':
    main()
