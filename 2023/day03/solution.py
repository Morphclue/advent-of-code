import re


def read_file(file_path='input.txt'):
    with open(file_path) as file:
        return [line.strip() for line in file.readlines()]


def has_neighbour(x_pos, y_pos, length, input_list, regex):
    return any(
        re.match(regex, input_list[y + y_pos][x + x_pos])
        for y in range(-1, 2)
        for x in range(-1, length + 1)
        if 0 <= y + y_pos < len(input_list) and 0 <= x + x_pos < len(input_list[y + y_pos])
    )


def extract_numbers(line):
    return [
        {
            'start': match.start(),
            'length': match.end() - match.start(),
            'value': int(match.group())
        }
        for match in re.finditer(r"\d+", line)
    ]


def calculate_sum(number_positions, input_lines):
    return sum(
        number_info['value']
        for row_index, positions_row in enumerate(number_positions)
        for number_info in positions_row
        if has_neighbour(number_info['start'], row_index, number_info['length'], input_lines, r'[^\d.]')
    )


def part1():
    input_lines = read_file()
    number_positions = [extract_numbers(line) for line in input_lines]
    total = calculate_sum(number_positions, input_lines)
    print(f'Part1: {total}')


if __name__ == '__main__':
    part1()
