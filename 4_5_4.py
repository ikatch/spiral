def main():
    V = []

    V.append(0.1)
    V.append(0.2)
    V.append(0.3)
    V[2] = 0.4
    print(*V)

    V.insert(2, 0.8)
    print(*V)

    V.pop(1)
    print(*V)

    V.append(0.9)
    print(*V)


if __name__ == '__main__':
    main()
