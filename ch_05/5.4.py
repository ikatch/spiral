# ALDS1_4_C: Dictionary
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_4_C
M = 1046527

dict_char = {
    'A':1,
    'C':2,
    'G':3,
    'T':4
}


def get_key(word:str) -> int:
    sum = 0
    p = 1
    for w in list(word):
        sum += p * dict_char[w]
        p *= 5
    return sum


def h1(key:int) -> int:
    return key % M


def h2(key:int) -> int:
    return 1 + (key % (M-1))


def h(key:int, i:int) -> int:
    return (h1(key=key) + i * h2(key=key)) % M


def main():
    n = int(input())
    T = {}

    for _ in range(n):
        cmd, word = input().split()
        key = get_key(word=word)
        if cmd == 'insert':
            T[key] = word
        else:
            if T.__contains__(key):
                print('yes')
            else:
                print('no')


if __name__ == '__main__':
    main()
