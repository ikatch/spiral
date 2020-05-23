import math
import random


def find_maximum(A: list, l: int, r: int) -> int:
    m = math.ceil((l + r) / 2)
    if l == r - 1:
        return A[l]
    else:
        u = find_maximum(A=A, l=l, r=m)
        v = find_maximum(A=A, l=m, r=r)
        x = max(u, v)
    return x


def main():
    A = [random.randint(0, 99) for _ in range(10)]
    print(A)
    print(find_maximum(A=A, l=0, r=len(A)))


if __name__ == '__main__':
    main()
