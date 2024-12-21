def read_file(file_path='input.txt'):
    with open(file_path) as file:
        return file.read()


def parse_map(map_string):
    return [list(map(int, line)) for line in map_string.strip().split('\n')]


def find_trailheads(map_data):
    trailheads = []
    for row in range(len(map_data)):
        for col in range(len(map_data[0])):
            if map_data[row][col] == 0:
                trailheads.append((row, col))
    return trailheads


def calculate_score(map_data, start):
    rows, cols = len(map_data), len(map_data[0])
    queue = [start]
    visited = set()
    reachable_nines = set()

    while queue:
        x, y = queue.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if map_data[x][y] == 9:
            reachable_nines.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if map_data[nx][ny] == map_data[x][y] + 1:
                    queue.append((nx, ny))

    return len(reachable_nines)


def calculate_total_score(map_string):
    map_data = parse_map(map_string)
    trailheads = find_trailheads(map_data)
    return sum(calculate_score(map_data, trailhead) for trailhead in trailheads)


def calculate_rating(map_data, start):
    rows, cols = len(map_data), len(map_data[0])
    stack = [(start, 0)]
    trail_count = 0

    while stack:
        (x, y), current_height = stack.pop()

        if map_data[x][y] == 9:
            trail_count += 1
            continue

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if map_data[nx][ny] == current_height + 1:
                    stack.append(((nx, ny), map_data[nx][ny]))

    return trail_count


def calculate_total_rating(map_string):
    map_data = parse_map(map_string)
    trailheads = find_trailheads(map_data)
    return sum(calculate_rating(map_data, trailhead) for trailhead in trailheads)


def main():
    map_input = read_file()
    print(f"Part 1: {calculate_total_score(map_input)}")
    print(f"Part 2: {calculate_total_rating(map_input)}")


if __name__ == '__main__':
    main()
