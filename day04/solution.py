def read_file(file_path='input.txt'):
    with open(file_path) as file:
        return file.readlines()


def part2():
    cards = read_file()
    copies = [1] * len(cards)
    for i, card in enumerate(cards):
        win, scratches = map(lambda x: list(map(int, x.strip().split())), card.split(":")[1].split("|"))
        matches = sum(1 for scratch in scratches if scratch in win)
        for j in range(i + 1, i + matches + 1):
            copies[j] += copies[i]

    return sum(copies)


if __name__ == '__main__':
   print(part2())