import re

# test variables
s = "mul(9,10)mul(101, 255)do()don't()"
t = "mul(6,9)"
u = "from()$why()#^mul(101,15);$^from()-!mul(570,448)/?(]who()/how()$-{mul(621,492)@?don't()who()}>*#mul(659,911))how()what():)<(do()from()-)%mul(134,954)select()mul(572,608)why()-)$+mul(392,779)"
v = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def format_data(file_path: str) -> list[str]:
    with open(file_path, "r") as data:
        return data.read()

def find_fixed(instruction: str) -> list[str]:
    pattern = re.compile(r"do\(\)|don't\(\)|mul\([0-9]{1,3}\s?,\s?[0-9]{1,3}\)")
    return pattern.findall(instruction)

def mul(instruction: str) -> int:
    """Perform mul(x, y)"""
    pattern = r"([0-9]{1,3}\s?,\s?[0-9]{1,3})"
    numbers = list(map(int, re.search(pattern, instruction)[0].split(',')))
    return numbers[0] * numbers[1]

def mul_fixed(instructions: list[str]) -> int:
    """multiply pairs of integers in strings, e.g. ['961,791', '320,807', '425,375', '310,951', '434,652']"""
    total = 0
    valid_instructions: list[str] = find_fixed(instructions)
    multiply = True
    for val in range(0, len(valid_instructions)):
        if valid_instructions[val] == "don't()":
            multiply = False
        elif valid_instructions[val] == "do()":
            multiply = True
        if "mul(" in valid_instructions[val] and multiply:
            total += mul(valid_instructions[val])
    return total

if __name__ == "__main__":
    file_path =  r"./2024/Day 3/input2.txt"
    parsed_data = format_data(file_path)
    print(mul_fixed(parsed_data))
    # answer is 85508223
