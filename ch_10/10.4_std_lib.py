# ALDS1_9_C: Priority Queue
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_9_C
import heapq


def main() -> None:
    S = []
    while True:
        cmd = list(input().split())
        if cmd[0] == 'insert':
            key = int(cmd[1])
            heapq.heappush(S, - key)
        elif cmd[0] == 'extract':
            print(- heapq.heappop(S))
        elif cmd[0] == 'end':
            break
        else:
            raise Exception('un-known command')
    return None


if __name__ == '__main__':
    main()
