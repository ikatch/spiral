import heapq


def main() -> None:
    PQ = []

    heapq.heappush(PQ, -1)
    heapq.heappush(PQ, -8)
    heapq.heappush(PQ, -3)
    heapq.heappush(PQ, -5)
    
    print(-heapq.heappop(PQ), end=' ')

    print(-heapq.heappop(PQ), end=' ')

    heapq.heappush(PQ, -11)

    print(-heapq.heappop(PQ), end=' ')

    print(-heapq.heappop(PQ))

    return None


if __name__ == '__main__':
    main()
