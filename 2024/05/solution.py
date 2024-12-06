from collections import defaultdict
from graphlib import TopologicalSorter

def read_file(file_path='input.txt'):
    with open(file_path) as file:
        data = file.read().strip().split('\n\n')
        rules = data[0].splitlines()
        updates = [list(map(int, line.split(','))) for line in data[1].splitlines()]
    return rules, updates

def parse_rules(rules):
    graph = defaultdict(set)
    for rule in rules:
        before, after = map(int, rule.split('|'))
        graph[after].add(before)
    return graph

def create_subgraph(graph_raw, pages):
    pages_set = set(pages)
    return {page: graph_raw[page].intersection(pages_set) for page in pages_set if page in graph_raw}

def validate_and_process_updates(graph_raw, updates):
    valid_sum = 0
    fixed_sum = 0

    for pages in updates:
        sub_graph = create_subgraph(graph_raw, pages)
        order = list(TopologicalSorter(sub_graph).static_order())
        mid_value = pages[len(pages) // 2] if order == pages else order[len(pages) // 2]
        valid_sum += mid_value if order == pages else 0
        fixed_sum += mid_value if order != pages else 0
    return valid_sum, fixed_sum

def main():
    rules, updates = read_file()
    graph_raw = parse_rules(rules)
    valid_sum, fixed_sum = validate_and_process_updates(graph_raw, updates)
    print("Part 1:", valid_sum)
    print("Part 2:", fixed_sum)

if __name__ == "__main__":
    main()
