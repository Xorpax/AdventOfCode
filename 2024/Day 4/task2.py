def find_xmas(data: list[str]) -> int:
    """find 2 MAS in an X-shape:
    M.S M.M S.M S.S
    .A. .A. .A. .A.
    M.S S.S S.M M.M
    """
    counter = 0
    for line in range(len(data)):
        for char in range(len(data[line])):
            if data[line][char] == "M" and char + 2 < len(data[line]) and line + 2 < len(data) and data[line + 1][char + 1] == "A" and data[line + 2][char + 2] == "S":
                if (data[line + 2][char] == "M" and data[line][char + 2] == "S") or (data[line + 2][char] == "S" and data[line][char + 2] == "M"):
                    counter += 1
            elif data[line][char] == "S" and char + 2 < len(data[line]) and line + 2 < len(data) and data[line + 1][char + 1] == "A" and data[line + 2][char + 2] == "M":
                if (data[line + 2][char] == "S" and data[line][char + 2] == "M") or (data[line + 2][char] == "M" and data[line][char + 2] == "S"):
                    counter += 1
    return counter

if __name__ == "__main__":
    with open(r".\2024\Day 4\input1.txt", "r") as file:
        data = file.read().split("\n")
    print(find_xmas(data))
    # answer is 1873
