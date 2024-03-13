import copy

if __name__ == '__main__':
    with open("level6_5.in", "r") as file:
        n = int(next(file))
        m = []
        for i in range(n):
            m.append(next(file).strip())
        n_crd = int(next(file))
        with open("result.out", "w") as f:
            for i in range(n_crd):
                a, b = [int(x.strip()) for x in next(file).split(',')]
                x, y = a, b
                dirs8 = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
                dirs4 = [[-1, 0], [0, 1], [1, 0], [0, -1]]
                visited = [(a, b)]
                queue = [(a, b)]
                min_x, min_y, max_x, max_y = x, y, x, y
                while len(queue) != 0:
                    x, y = queue.pop(0)
                    for dir in dirs4:
                        new_x = x + dir[0]
                        new_y = y + dir[1]
                        if (new_x, new_y) not in visited and m[new_y][new_x] == 'L':
                            min_x = min(min_x, new_x)
                            min_y = min(min_y, new_y)
                            max_x = max(max_x, new_x)
                            max_y = max(max_y, new_y)
                            queue.append((new_x, new_y))
                            visited.append((new_x, new_y))
                op_size = max(max_x-min_x, max_y-min_y)
                print(op_size)

                pad = 250

                sea = [[0 for i in range(2*pad)] for j in range(2*pad)]
                for point in visited:
                    sea[pad+point[1]][pad+point[0]] = 1

                for k in range(op_size):
                    sea_copy = copy.deepcopy(sea)
                    for x in range(1, 2*pad-1):
                        for y in range(1, 2*pad-1):
                            if sea[y][x] == 0:
                                has_neigh = False
                                for dir in dirs4:
                                    new_x = x + dir[0]
                                    new_y = y + dir[1]
                                    if sea[new_y][new_x] == 1:
                                        has_neigh = True
                                if has_neigh:
                                    sea_copy[y][x] = 1
                    sea = copy.deepcopy(sea_copy)

                for k in range(op_size):
                    sea_copy = copy.deepcopy(sea)
                    for x in range(1, 2 * pad - 1):
                        for y in range(1, 2 * pad - 1):
                            if sea[y][x] == 1:
                                has_neigh = False
                                for dir in dirs4:
                                    new_x = x + dir[0]
                                    new_y = y + dir[1]
                                    if sea[new_y][new_x] == 0:
                                        has_neigh = True
                                if has_neigh:
                                    sea_copy[y][x] = 0
                    sea = copy.deepcopy(sea_copy)

                visited = []
                for x in range(1, 2 * pad - 1):
                    for y in range(1, 2 * pad - 1):
                        if sea[y][x] == 1:
                            visited.append((x-pad, y-pad))
                print(visited)

                contour = []
                for x in range(n):
                    for y in range(n):
                        if (x, y) not in visited:
                            has_neigh = False
                            for dir in dirs4:
                                new_x = x + dir[0]
                                new_y = y + dir[1]
                                if (new_x, new_y) in visited:
                                    has_neigh = True
                            if has_neigh and (x, y) not in contour:
                                contour.append((x, y))
                contour_ord = [contour[0]]
                cur_dir = 1
                curr = contour[0]
                while len(contour_ord) != len(contour):
                    new_x = curr[0] + dirs8[cur_dir][0]
                    new_y = curr[1] + dirs8[cur_dir][1]
                    if (new_x, new_y) in contour:
                        cur_dir = (cur_dir + 4) % 8
                        curr = (new_x, new_y)
                        if curr == contour[0]:
                            break
                        contour_ord.append((new_x, new_y))

                    cur_dir = (cur_dir + 1) % 8
                print(len(contour_ord), len(contour))
                for (x, y) in contour_ord:
                    f.write(f"{x},{y} ")
                f.write("\n")