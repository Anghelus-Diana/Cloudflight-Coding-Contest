if __name__ == '__main__':
    with open("level6_example.in", "r") as file:
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
                while len(queue) != 0:
                    x, y = queue.pop(0)
                    for dir in dirs4:
                        new_x = x + dir[0]
                        new_y = y + dir[1]
                        if (new_x, new_y) not in visited and m[new_y][new_x] == 'L':
                            queue.append((new_x, new_y))
                            visited.append((new_x, new_y))
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