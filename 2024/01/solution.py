from collections import Counter


def read_file(file_path='input.txt'):
    with open(file_path) as file:
        return file.readlines()

def part2(data):
    rows = [list(map(int, line.split())) for line in data]
    left = [row[0] for row in rows]
    right = [row[1] for row in rows]
    right_count = Counter(right)
    similarity_score = sum(value * right_count[value] for value in left)
    return similarity_score

if __name__ == '__main__':
    print(f"Part 2: {part2(read_file())}")
