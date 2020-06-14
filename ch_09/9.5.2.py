
def print_dict(T: dict) -> None:
    print('{}'.format(T.__len__()))
    for t in T:
        print('{} --> {}'.format(t, T[t]))
    return None


def main() -> None:
    T = {}

    T['red'] = 32
    T['blue'] = 688
    T['yellow'] = 122

    T['blue'] += 312

    print_dict(T=T)

    T.update([('zebra', 101010)])
    T.update([('white', 0)])
    T.pop('yellow')

    print_dict(T=T)

    t = 'red'
    print('{} --> {}'.format(t, T[t]))

    return None


if __name__ == '__main__':
    main()
