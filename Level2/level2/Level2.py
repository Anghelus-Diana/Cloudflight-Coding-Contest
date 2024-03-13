if __name__ == '_main_':
    with open("level2_example.in", "r") as file:
        n = int(next(file))
        m = []
        for i in range(n):
            m.append(next(file).strip())
        n_crd = int(next(file))
        with open("result.out", "w") as f:
            for i in range(n_crd):
                lst = [x for x in next(file).split()]
                a, b = [int(x) for x in lst[0].split(',')]
                c, d = [int(x) for x in lst[1].split(',')]
                visited = []
                queue = [(a, b)]
                dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                found = 0
                while len(queue) != 0:
                    x, y = queue.pop()
                    if (x, y) == (c, d):
                        f.write("SAME\n")
                        found = 1
                    visited.append((x, y))
                    for j in range(4):
                        new_x = x + dirs[j][0]
                        new_y = y + dirs[j][1]
                        if (new_x, new_y) not in visited and m[new_y][new_x] == 'L':
                            queue.append((new_x, new_y))
                if found == 0:
                    f.write("DIFFERENT\n")
