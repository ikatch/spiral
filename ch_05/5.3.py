# ALDS1_4_B: Binary Search
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_4_B
import math


def binary_search(A:list, n:int, key:int) -> bool:
     left = 0
     right = n

     while left < right:
         mid = math.floor((left + right) / 2)
         if key == A[mid]:
             return True
         elif key > A[mid]:
             left = mid + 1
         else:
             right = mid
     return False


def main():
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))
    C = 0

    for t in T:
        if binary_search(A=S, n=n, key=t):
            C += 1

    print(C)


if __name__ == '__main__':
    main()
