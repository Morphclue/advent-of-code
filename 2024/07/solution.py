from operator import add, mul

operations = [add, mul]

def read_file(file_path='input.txt'):
    with open(file_path) as file:
        return [line.strip() for line in file.readlines()]

def solve(solution, values, current, i=1):
    if i == len(values):
        return current == solution

    return any(
        solve(solution, values, operation(current, values[i]), i + 1)
        for operation in operations
    )

def process_data(data):
    result = 0
    for line in data:
        solution, values = line.split(": ")
        solution = int(solution)
        values = list(map(int, values.split()))
        if solve(solution, values, values[0]):
            result += solution
    return result


def main():
    data = read_file()
    print(f"Part1: {process_data(data)}")
    operations.append(lambda a, b: int(str(a) + str(b)))
    print(f"Part2: {process_data(data)}")


if __name__ == '__main__':
    main()