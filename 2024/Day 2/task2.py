def parse_input(file_path: str) -> list[int]:
    with open(file_path, "r") as input_file:
        reports = [list(map(int, line.split())) for line in input_file]
        return reports

def is_safe(report: list) -> bool:
    # if asc: next - curr > 0
    # else: next - curr < 0
    # if 0 < abs(dist) < 4 and (asc or desc)
    ascending = all(curr < next for curr, next in zip(report, report[1:]))

    descending = all(curr > next for curr, next in zip(report, report[1:]))
    
    return (ascending or descending) and all(0 < abs(next - curr) < 4 for next, curr in zip(report, report[1:]))
        
def count_safe(reports: list[list[int]]) -> int:
    counter = 0
    for report in reports:
        if is_safe(report) or remove_level(report):
            counter += 1
    return counter

# to check if a report is safe, remove one level at a time and validate

def remove_level(report: list[int]) -> bool:
    for level in range(len(report)):
        report_copy = report[:]
        del report_copy[level]
        if is_safe(report_copy):
            return True
    return False

if __name__ == "__main__":
    fp = r"2024\Day 2\input2.txt"
    parsed_data = parse_input(fp)
    print(count_safe(parsed_data))

