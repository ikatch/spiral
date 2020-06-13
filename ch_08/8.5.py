# ALDS1_7_D: Reconstruction of the Tree
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_7_D


def reconstruct(left_idx: int, right_idx: int) -> None:
    if left_idx >= right_idx:
        return None
    else:
        c = pre_parse.pop(0)
        middle_idx = in_parse.index(c)

        reconstruct(left_idx=left_idx, right_idx=middle_idx)
        reconstruct(left_idx=middle_idx+1, right_idx=right_idx)

        post_parse.append(c)
    return None


def main() -> None:
    n = int(input())

    global pre_parse
    global in_parse
    global post_parse

    pre_parse = list(map(int, input().split()))
    in_parse = list(map(int, input().split()))
    post_parse = []

    reconstruct(left_idx=0, right_idx=n)

    print(*post_parse)

    return None


if __name__ == '__main__':
    main()
