# ALDS1_9_C: Priority Queue
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_9_C
INFTY = 1 << 30


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
        # largest: right or larger one in original and left
        if right_id <= H and self.A[right_id - 1] > self.A[largest_id - 1]:
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

    def heap_increase_key(self, id: int, key: int) -> None:
        if key < self.A[id - 1]:
            raise Exception('new key is lower than current one')
        else:
            pass
        self.A[id - 1] = key
        while id > 1 and self.A[self.parent(id=id) - 1] < self.A[id - 1]:
            self.A[self.parent(id=id) - 1], self.A[id - 1] = self.A[id - 1], self.A[self.parent(id=id) - 1]
            id = self.parent(id=id)
        return None

    def insert(self, key) -> None:
        self.A.append(-INFTY)
        self.heap_increase_key(id=self.A.__len__(), key=key)
        return None

    def heap_extract_max(self):
        if self.A.__len__() < 1:
            raise Exception('heap under flow')
        else:
            max_val = self.A[0]
            self.A[0] = self.A[-1]
            self.A.pop()
            self.max_heapify(id=1)
        return max_val


class PriorityQueue(MaximumHeap):
    def __init__(self):
        super().__init__()


def main() -> None:
    pq = PriorityQueue()
    while True:
        cmd = list(input().split())
        if cmd[0] == 'insert':
            key = int(cmd[1])
            pq.insert(key=key)
        elif cmd[0] == 'extract':
            print(pq.heap_extract_max())
        elif cmd[0] == 'end':
            return None
        else:
            raise Exception('un-known command')


if __name__ == '__main__':
    main()
