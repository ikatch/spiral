# ALDS1_4_A: Linear Search
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_4_A


def search(A:list, n:int, key:int) -> bool:
     A.append(key)
     for i in range(len(A)):
         if A[i] == key:
             break
         else:
             continue

     A.pop()
     return i != n


def main():
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))
    C = 0

    for t in T:
        if search(A=S, n=n, key=t):
            C += 1

    print(C)


if __name__ == '__main__':
    main()
