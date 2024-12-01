def read_file(file_path='input.txt'):
    with open(file_path) as file:
        return file.read().strip().split("\n\n")


def transform(step, mapping):
    for destination, source, range_length in mapping:
        if source <= step < source + range_length:
            step = destination + (step - source)
            break
    return step


def process_seeds(seeds, maps):
    lowest_location = float("inf")
    for seed in seeds:
        for m in maps:
            seed = transform(seed, m)
        lowest_location = min(lowest_location, seed)
    return lowest_location


def part1():
    file = read_file()
    seeds = [int(x) for x in file[0].replace("seeds: ", "").split(" ")]
    maps_raw = [file[i].splitlines()[1::] for i in range(1, 8)]
    maps = [[list(map(int, x.split(" "))) for x in lines] for lines in maps_raw]
    result = process_seeds(seeds, maps)
    print(result)


if __name__ == '__main__':
    part1()
