import re

# test variables
# s = "mul(9,10)mul(101, 255)"
# t = "mul(6,9)"
# q = "from()$why()#^mul(101,15);$^from()-!mul(570,448)/?(]who()/how()$-{mul(621,492)@?don't()who()}>*#mul(659,911))how()what():)<(do()from()-)%mul(134,954)select()mul(572,608)why()-)$+mul(392,779)"

# def format_data(file_path: str) -> list[str]:
#     with open(file_path, "r") as data:
#         return data.readlines()

def format_data(file_path: str) -> str:
    with open(file_path, "r") as data:
        return data.read()

def find_mul(instruction: str) -> list[str]:
    """return a list of pairs of valid numbers, e.g. ['101,15', '570,448', '621,492', '659,911', '134,954', '572,608', '392,779']"""
    pattern = re.compile(r"mul\(([0-9]{1,3}\s?,\s?[0-9]{1,3})\)")
    return pattern.findall(instruction)

def mul(instructions: list[str]) -> int:
    """multiply pairs of integers in strings, e.g. ['961,791', '320,807', '425,375', '310,951', '434,652']"""
    total = 0
    # for instruction in instructions:
    valid_instructions: list[str] = find_mul(instructions)
    total += sum([num1 * num2 for num1, num2 in [list(map(int, pair.split(","))) for pair in valid_instructions]])
    return total

if __name__ == "__main__":
    file_path =  r"./2024/Day 3/input1.txt"
    parsed_data = format_data(file_path)
    part1 = mul(parsed_data)
    print(part1)
    # answer is 187825547
