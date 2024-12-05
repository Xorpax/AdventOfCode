import math
import time

def format_data(file_path: str) -> tuple[list[int], list[int]]:
    with open(file_path, "r") as data:
        lines = data.readlines()
        order = [tuple(map(int, line.strip().split("|"))) for line in lines if "|" in line]
        updates = [tuple(map(int, line.strip().split(","))) for line in lines if "," in line]
        return order, updates
    
def is_in_order(update, order):
    return all((p1, p2) in order for p1, p2 in zip(update, update[1:]))

def order(update, order):
    temp = update[:]
    for p1, p2 in zip(temp, temp[1:]):
        if (p1, p2) not in order:
            p1, p2 = p2, p1


if __name__ == "__main__":
    start = time.time()
    file_path = r".\2024\Day 5\input.txt"
    # file_path = r".\2024\Day 5\test.txt"
    order, updates = format_data(file_path)
    total = 0
    for update in updates:
        if is_in_order(update, order):
            l_update = len(update)
            total += update[math.ceil(l_update / 2 ) - 1]

    print(total)
    end = time.time()
    print(f"{(end - start) * 1000:.4f}ms")
    # answer is 4689
