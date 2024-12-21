from collections import defaultdict


def read_file(file_path='input.txt'):
    with open(file_path, 'r') as file:
        return file.read().strip().split("\n")


def inbounds(map_data, x, y):
    return 0 <= x < len(map_data[0]) and 0 <= y < len(map_data)


def anti_nodes(map_data, p1, p2):
    p1_pts = set()
    p2_pts = {p1, p2}

    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1

    if inbounds(map_data, x1 - dx, y1 - dy):
        p1_pts.add((x1 - dx, y1 - dy))
    if inbounds(map_data, x2 + dx, y2 + dy):
        p1_pts.add((x2 + dx, y2 + dy))

    current_x, current_y = x1, y1
    while True:
        current_x -= dx
        current_y -= dy
        if not inbounds(map_data, current_x, current_y):
            break
        p2_pts.add((current_x, current_y))

    current_x, current_y = x1, y1
    while True:
        current_x += dx
        current_y += dy
        if not inbounds(map_data, current_x, current_y):
            break
        p2_pts.add((current_x, current_y))

    return p1_pts, p2_pts


def find_anti_nodes(map_data):
    lut = defaultdict(list)
    for y, row in enumerate(map_data):
        for x, char in enumerate(row):
            if char != ".":
                lut[char].append((x, y))

    p1, p2 = set(), set()
    for positions in lut.values():
        if len(positions) < 2:
            continue
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                p1_pts, p2_pts = anti_nodes(map_data, positions[i], positions[j])
                p1.update(p1_pts)
                p2.update(p2_pts)

    return p1, p2


def main():
    map_data = read_file()
    p1, p2 = find_anti_nodes(map_data)
    print(f"Part 1: {len(p1)}")
    print(f"Part 2: {len(p2)}")


if __name__ == "__main__":
    main()
