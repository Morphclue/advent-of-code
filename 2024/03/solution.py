import re

def read_file(file_path='input.txt'):
    with open(file_path) as file:
        return file.read()


def calculate_results(data):
    data = "do()" + data + "don't()"
    cleaned_data = re.sub(r"don't\(\).*?do\(\)", "do()", data, flags=re.DOTALL)
    matches = re.findall(r"mul\((\d+),(\d+)\)", cleaned_data)
    return sum(int(x) * int(y) for x, y in matches)


if __name__ == "__main__":
    result = calculate_results(read_file())
    print("Result:", result)