if __name__ == '_main_':
    with open("level1_4.in", "r") as file:
        n = int(next(file))
        m = []
        for i in range(n):
            m.append(next(file).strip())
        n_crd = int(next(file))
        with open("level1_1.out", "w") as f:
            for i in range(n_crd):
                x, y = [int(x.strip()) for x in next(file).split(',')]
                f.write(m[x][y])
                f.write('\n')