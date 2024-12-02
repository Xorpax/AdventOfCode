def get_input(file_path: str) -> list[int]:
    print(file_path)
    with open(file_path, "r") as input_file:
        data = [row.strip().split() for row in input_file.readlines()]
        data = [[int(num) for num in row] for row in data]
        return data

def check_report(report: list[int]) -> bool:
    asc = False
    report_length = len(report)
    max_level = max(report)
    min_level = min(report)
    print(report)
    if report.index(max_level) > report.index(min_level):
        asc = True
    print(asc)

    for level in range(1, report_length):
        current_level = report[level]
        previous_level = report[level - 1]
        dist = current_level - previous_level
        if asc:
            if dist <= 0 or dist > 3:
                return False
        else:
            if dist >= 0 or dist < -3:
                return False
    return True
            


def count_safe(reports: list[list[int]]) -> int:
    counter = 0
    for report in reports:
        if check_report(report):
            counter += 1


    return counter


fp = r"2024\Day 2\Task 1\input.txt"
parsed_data = get_input(fp)
safe = count_safe(parsed_data)
print(safe)
