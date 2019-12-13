def multiplicationTable():
    """99乘法表"""
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{}x{}={:<2d}\t".format(j, i, i * j), end="")

        print()


if __name__ == '__main__':
    multiplicationTable()
