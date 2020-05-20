# ALDS1_2_C: Stable Sort
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_C
import copy

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


def bubble(A:list) -> list:
    N: int = len(A)

    for i in range(0, N, 1):
        for j in reversed(range(i+1, len(A), 1)):
            if A[j].value < A[j-1].value:
                A[j], A[j-1] = A[j-1], A[j]
    return A


def selection(A:list) -> list:
    N: int = len(A)

    for i in range(0, N, 1):
        min_j = i
        for j in range(i, N, 1):
            if A[j].value < A[min_j].value:
                min_j = j

        A[i], A[min_j] = A[min_j], A[i]
    return A


def print_card(A:list) -> None:
    for a in A[:-1]:
        print('{}{}'.format(a.suit, a.value), end=' ')
    print('{}{}'.format(A[-1].suit, A[-1].value))


def is_stable(C_bubble:list, C_selection:list) -> bool:
    for i in range(0, len(C_bubble), 1):
        if C_bubble[i].suit != C_selection[i].suit:
            return False
    return True


def main():
    N: int = int(input())
    C = [Card(suit=c[:1], value=c[1:]) for c in list(input().split())]

    C_bubble = copy.deepcopy(x=C)
    C_selection = copy.deepcopy(x=C)

    C_bubble = bubble(A=C_bubble)
    C_selection = selection(A=C_selection)

    print_card(A=C_bubble)
    print('Stable')
    print_card(A=C_selection)
    if is_stable(C_bubble=C_bubble, C_selection=C_selection):
        print('Stable')
    else:
        print("Not stable")


if __name__ == '__main__':
    main()
