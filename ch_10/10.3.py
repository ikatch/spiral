# ALDS1_9_B: Maximum Heap
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_9_B


class CompleteBinaryTree:
    A = []

    def __init__(self):
        pass

    def parent(self, id: int) -> int:
        return id // 2

    def left(self, id: int) -> int:
        return 2 * id

    def right(self, id: int) -> int:
        return 2 * id + 1


class MaximumHeap(CompleteBinaryTree):

    def __init__(self):
        super().__init__()

    def max_heapify(self, id: int) -> None:
        H = self.A.__len__()
        left_id = self.left(id=id)
        right_id = self.right(id=id)
        # find id which has the largest value
        if left_id <= H and self.A[left_id - 1] > self.A[id - 1]:  # largest: original or left
            largest_id = left_id
        else:
            largest_id = id
        if right_id <= H and self.A[right_id - 1] > self.A[
            largest_id - 1]:  # largest: right or larger one in original and left
            largest_id = right_id
        else:
            pass
        # swap between original and largest
        if largest_id != id:
            self.A[id - 1], self.A[largest_id - 1] = self.A[largest_id - 1], self.A[id - 1]
            self.max_heapify(id=largest_id)
        return None

    def build_max_heap(self) -> None:
        H = self.A.__len__()
        for id in range(H // 2, 0, -1):
            self.max_heapify(id=id)
        return None


def main() -> None:
    H = int(input())
    A = list(map(int, input().split()))

    mh = MaximumHeap()
    mh.A = A
    mh.build_max_heap()
    print(' ', end='')
    print(*mh.A)
    return None


if __name__ == '__main__':
    main()
