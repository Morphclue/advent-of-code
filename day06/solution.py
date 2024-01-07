import math
import re


def read_file(file_path='input.txt'):
    with open(file_path) as file:
        return [line.strip() for line in file.readlines()]


def calculate_wins(times, distances):
    count = 1
    for time, distance in zip(times, distances):
        wins = 0
        speed = 0
        for i in range(1, time):
            speed += 1
            travel_distance = (time - i) * speed
            if travel_distance > distance:
                wins += 1
        count *= wins
    return count


def part1():
    input_lines = read_file()
    times = [int(time) for time in re.findall(r'\d+', input_lines[0])]
    distances = [int(distance) for distance in re.findall(r'\d+', input_lines[1])]
    result = calculate_wins(times, distances)
    print(f'Part1: {result}')


def part2():
    input_lines = read_file()
    time = int(''.join(re.findall(r'\d+', input_lines[0])))
    distance = int(''.join(re.findall(r'\d+', input_lines[1])))
    sqrt_val = math.sqrt(time ** 2 - 4 * distance)
    result = time - 2 * math.ceil((time - sqrt_val) / 2) + 1
    print(f'Part2: {result}')


if __name__ == '__main__':
    part1()
    part2()
