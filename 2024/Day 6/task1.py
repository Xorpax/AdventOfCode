import time

# test = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

# obstacle_north = """....#.....
# ....^....#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#..."""

# obstacle_east = """....#.....
# ........>#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#..."""

# obstacle_south = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#......v.
# ........#.
# #.........
# ......#..."""

# obstacle_west = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#<.."""

# no_obstacle = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#v.."""

# can_move_south = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #......v..
# ......#..."""

# can_move_west = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #......<..
# ......#..."""

directions: dict[str, int] = {
    "^": ("north", -1),
    ">": ("east", 1),
    "v": ("south", 1),
    "<": ("west", -1),
}


def format_data(file_path: str) -> list[str]:
    with open(file_path, "r") as data:
        return data.readlines()

def turn(char: str) -> str:
    states = list(directions.keys())
    start_index = 0
    end_index = len(states) - 1
    current_index = states.index(char)
    if current_index == end_index:
        return states[start_index]
    return states[current_index + 1]

def go_forward(puzzle_map: list[str], char: str, x, y) -> list[str]:
    """check if can move forward and return the updated map"""
    currently_facing = directions[char][0]
    offset = directions[char][1]
    current_line = puzzle_map[y]
    go_x, go_y = False, False

    # print(f"{currently_facing=}")
    try:
        if currently_facing == "north" or currently_facing == "south":
            next_position = puzzle_map[y + offset][x]
            go_y = True
            # print("moving vertical")
            # print(y + offset)
        elif currently_facing == "east" or currently_facing == "west":
            next_position = puzzle_map[y][x + offset]
            go_x = True
            # print("moving horizontal")
    except IndexError:
        # guard can exit the map
        puzzle_map[y] = puzzle_map[y].replace(char, "X")
        return puzzle_map
    else:
        # move forward or turn 90 degrees right in case of an obstacle
        # print(f"{next_position=}")
        #obstacle
        # print(f"{go_x=}, {go_y=}")
        if next_position == "#":
            turned_char = turn(char)
            puzzle_map[y] = puzzle_map[y].replace(char, turned_char)
            # print(f"line after turning: {puzzle_map[y]}")
            # return puzzle_map 
        elif go_x:
            line_structure = list(current_line)
            # print(f"{line_structure=}")
            char_index = line_structure.index(char)
            # print(f"{char_index=}")
            line_structure[char_index] = "X"
            line_structure[char_index + offset] = char
            new_line = "".join(line_structure)
            # print(f"{line_structure=}")
            # print(f"{current_line=}")
            # print(f"{new_line=}")
            puzzle_map[y] = new_line
        elif go_y:
            current_line_structure = list(current_line)
            # print(f"{current_line_structure=}")
            
            next_line = puzzle_map[y + offset]
            # print(f"{next_line=}") 
            next_lines_structure = list(next_line)
            # print(f"{next_lines_structure=}")
            # print(f"{char=}")
            
            char_index = current_line_structure.index(char)
            # print(f"{char_index=}")
            next_lines_structure[char_index] = char
            # print(f"{next_lines_structure=}")
            new_line_string = "".join(next_lines_structure)
            # print(f"{new_line_string=}")
            # print(y + offset)
            puzzle_map[y + offset] = new_line_string
            # puzzle_map[y + offset] = next_lines_structure
            puzzle_map[y] = puzzle_map[y].replace(char, "X")
            # puzzle_map[y + offset] = "".join(next_lines_structure)
            # print(f"{puzzle_map[y + offset]=}")
            # next_line = "".join(next_lines_structure)
            # print(f"{next_line=}")
            # puzzle_map[y + offset] = next_line
            # print(f"{puzzle_map[y + offset]=}")
        return puzzle_map

def parse_map(puzzle_map: list[str]):
    states = list(directions.keys())
    coordinates: list[tuple[int, int]] = []
    while any(state in line for line in puzzle_map for state in states):
        for line in range(len(puzzle_map)):
            # print(puzzle_map[line])
            for x in range(len(puzzle_map[line])):
                current_char = puzzle_map[line][x]
                if current_char in states:
                    # print(f"found the guard on line: {line} x: {x}")
                    # print(f"{current_char=}")
                    # print(go_forward(puzzle_map, current_char, x, line))
                    puzzle_map = go_forward(puzzle_map, current_char, x, line)
                    # print("\n".join(puzzle_map))

    # # print(mark)
    # print("\n".join(puzzle_map))
    print("\n".join(puzzle_map).count("X"))

if __name__ == "__main__":
    # puzzle_map = obstacle_north.split("\n")
    # puzzle_map = obstacle_south.split("\n")
    # puzzle_map = obstacle_east.split("\n")
    # puzzle_map = obstacle_west.split("\n")
    # puzzle_map = no_obstacle.split("\n")
    # puzzle_map = can_move_south.split("\n")
    # puzzle_map = can_move_west.split("\n")
    filepath = r".\2024\Day 6\input1.txt"
    start = time.time()
    # puzzle_map = test.split("\n")
    puzzle_map = format_data(filepath)
    # print("\n".join(puzzle_map))
    parse_map(puzzle_map)
    end = time.time()
    print(f"elapsed: {(end - start):.3f}seconds")
    # answer is 4711 (part 1) in 4.x seconds (previous 14.x-15.x seconds)