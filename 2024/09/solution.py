def read_file(file_path='input.txt'):
    with open(file_path) as file:
        return file.read()

def check_sum(file_system):
    return sum(position * int(file_id) for position, file_id in enumerate(file_system) if file_id != '.')


def process_data(data):
    return [str(i // 2) if i % 2 == 0 else '.' for i, num in enumerate(data) for _ in range(int(num))]


def compact(file_system):
    block_pointer = len(file_system) - 1
    free_space_pointer = 0
    while block_pointer >= 0:
        if file_system[block_pointer] != '.':
            while free_space_pointer < len(file_system) and file_system[free_space_pointer] != '.':
                free_space_pointer += 1
            if block_pointer > free_space_pointer < len(file_system):
                file_system[free_space_pointer], file_system[block_pointer] = file_system[block_pointer], '.'
                free_space_pointer += 1
        block_pointer -= 1
    return file_system


def main():
    data = read_file()
    file_system = process_data(data)
    solution = compact(file_system)
    print(f"Part 1: {check_sum(solution)}")


if __name__ == '__main__':
    main()