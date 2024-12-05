import math

def format_data(file_path: str) -> tuple[list[int], list[int]]:
    with open(file_path, "r") as data:
        lines = data.readlines()
        order = [tuple(map(int, line.strip().split("|"))) for line in lines if "|" in line]
        updates = [list(map(int, line.strip().split(","))) for line in lines if "," in line]
        return order, updates
    
def is_in_order(update: list[int], order: list[tuple[int, int]]) -> bool:
    return all((p1, p2) in order for p1, p2 in zip(update, update[1:]))

def order_update(update: list[int], order: list[tuple[int, int]]) -> int:
    """Bubble sort on steroids :P"""
    temp = update[:]
    i = 0
    while not is_in_order(temp, order):
        for p1, p2 in zip(temp, temp[1:]):
            if i + 1 >= len(temp):
                i = 0
            if (p1, p2) not in order:
                temp[i], temp[i + 1] = temp[i + 1], temp[i]
            i += 1
    return temp[math.ceil(len(temp) / 2) - 1]

if __name__ == "__main__":
    file_path = r".\2024\Day 5\input.txt"
    # file_path = r".\2024\Day 5\test.txt"
    order, updates = format_data(file_path)
    part1, part2 = 0, 0
    for update in updates:
        if is_in_order(update, order):
            part1 += update[math.ceil(len(update) / 2 ) - 1]
        else:
            part2 += order_update(update, order)
    print(f"{part1=}") # answer is 4689
    print(f"{part2=}") # answer is 6336 
