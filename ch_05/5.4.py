# ALDS1_4_C: Dictionary
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_4_C
M = 1046527
NIL = -1
L = 14


def get_char(ch:str) -> int:
    if ch == 'A':
        return 1
    elif ch == 'C':
        return 2
    elif ch == 'G':
        return 3
    elif ch == 'T':
        return 4
    else:
        return 0


def get_key(word:str) -> float:
    sum = 0
    p = 1
    for w in list(word):
        sum += p * get_char(ch=w)
        p *= 5
    return sum


def h1(key:int) -> int:
    return key % M


def h2(key:int) -> int:
    return 1 + (key % (M-1))


def h(key:int, i:int) -> int:
    return (h1(key=key) + i * h2(key=key)) % M


def insert(T:list, word:str):
    key = get_key(word=word)
    i = 0
    while True:
        j = h(key=key, i=i)
        if T[j] == '':
            T[j] = key
            return j
        else:
            i += 1


def find(T:list, word:str) -> int:
    key = get_key(word=word)
    i = 0
    while True:
        j = h(key=key, i=i)
        if T[j] == key:
            return j
        elif T[j] == '':
            return NIL
        i += 1
    return NIL


def main():
    n = int(input())
    T = [''] * M

    for _ in range(n):
        cmd, word = input().split()
        if cmd[0] == 'i':
            insert(T=T, word=word)
        elif cmd[0] == 'f':
            if find(T=T, word=word) != NIL:
                print('yes')
            else:
                print('no')


if __name__ == '__main__':
    main()
