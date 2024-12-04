sample = """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX"""
        
def find_horizontal(data: list[str]) -> int:
    return sum(line.count("XMAS") + line.count("SAMX") for line in data)

def find_diagonal(data: list[str]) -> int:
    """We have the following possibilities:
    X... ...X S... ...S
    .M.. ..M. .A.. ..A.
    ..A. .A.. ..M. .M..
    ...S S... ...X X...
    """
    counter = 0
    for line in range(len(data)):
        for char in range(len(data[line])):
            if data[line][char] == "X" and line + 3 < len(data) and char + 3 < len(data[line]):
                if data[line + 1][char + 1] == "M" and data[line + 2][char + 2] == "A" and data[line + 3][char + 3] == "S":
                    counter += 1
            if data[line][char] == "X" and line + 3 < len(data) and char - 3 >= 0:
                if data[line + 1][char - 1] == "M" and data[line + 2][char - 2] == "A" and data[line + 3][char - 3] == "S":
                    counter += 1
            if data[line][char] == "S" and line + 3 < len(data) and char + 3 < len(data[line]):
                if data[line + 1][char + 1] == "A" and data[line + 2][char + 2] == "M" and data[line + 3][char + 3] == "X":
                    counter += 1
            if data[line][char] == "S" and line + 3 < len(data) and char - 3 >= 0:
                if data[line + 1][char - 1] == "A" and data[line + 2][char - 2] == "M" and data[line + 3][char - 3] == "X":
                    counter += 1
    return counter

def find_vertical(data: list[str]) -> int:
    """
    X... S... etc.
    M... A...
    A... M...
    S... X...
    """
    counter = 0
    number_of_lines = len(data)
    for line in range(len(data)):
        for char in range(len(data[line])):
            if data[line][char] == "X" and line + 3 < number_of_lines:
                if data[line + 1][char]== "M" and data[line + 2][char] == "A" and data[line + 3][char] == "S":
                    counter += 1
            if data[line][char] == "S" and line + 3 < number_of_lines:
                if data[line + 1][char] == "A" and data[line + 2][char] == "M" and data[line + 3][char] == "X":
                    counter += 1
    return counter

if __name__ == "__main__":
    with open(r".\2024\Day 4\input1.txt", "r") as file:
        data = file.read().split("\n")
    print(find_vertical(data) + find_horizontal(data) + find_diagonal(data))
    # answer is 2524
