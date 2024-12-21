from collections import Counter


def read_file(file_path='input.txt'):
    with open(file_path) as file:
        return list(map(int, file.read().strip().split()))


def split_stone(n):
    digits = str(n)
    mid = len(digits) // 2
    return int(digits[:mid]), int(digits[mid:])


def simulate_blinks(stones, blinks):
    stone_counts = Counter(stones)

    for _ in range(blinks):
        new_stone_counts = Counter()

        for stone, count in stone_counts.items():
            if stone == 0:
                new_stone_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                left, right = split_stone(stone)
                new_stone_counts[left] += count
                new_stone_counts[right] += count
            else:
                new_stone_counts[stone * 2024] += count

        stone_counts = new_stone_counts
    return sum(stone_counts.values())


def main():
    initial_stones = read_file()
    print("Part 1:", simulate_blinks(initial_stones, 25))
    print("Part 2:", simulate_blinks(initial_stones, 75))


if __name__ == '__main__':
    main()
