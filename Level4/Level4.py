if __name__ == '__main__':
    with open("level4_example.in", "r") as file:
        n = int(next(file))
        m = []
        for i in range(n):
            m.append(next(file).strip())
        n_crd = int(next(file))
        with open("result.out", "w") as f:
            for i in range(n_crd):
                parents = [[[] for j in range(n)] for i in range(n)]
                lst = [x for x in next(file).split()]
                a, b = [int(x) for x in lst[0].split(',')]
                c, d = [int(x) for x in lst[1].split(',')]
                visited = []
                queue = [(a, b)]
                dirs = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
                found = 0
                while len(queue) != 0:
                    x, y = queue.pop()
                    if (x, y) == (c, d):
                        break
                    visited.append((x, y))
                    for j in range(4):
                        new_x = x + dirs[j][0]
                        new_y = y + dirs[j][1]
                        if 0 <= new_x < n and 0 <= new_y < n:
                            if (new_x, new_y) not in visited and m[new_y][new_x] == 'W':
                                queue.append((new_x, new_y))
                                parents[new_y][new_x] = [x, y]
                path = []
                curr = [c, d]
                while not curr == [a, b]:
                    path.append(curr)
                    curr = parents[curr[1]][curr[0]]
                path.append([a, b])
                path.reverse()
                for curr in path:
                    f.write(f'{curr[0]},{curr[1]} ')
            f.write("\n")