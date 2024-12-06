import time

test = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

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

def go_forward(puzzle_map: list[str], char: str, x, y) -> tuple[list[str], tuple[int, int]]:
    """check if can move forward and return the updated map"""
    currently_facing = directions[char][0]
    offset = directions[char][1]
    current_line = puzzle_map[y]
    go_x, go_y = False, False

    try:
        if currently_facing == "north" or currently_facing == "south":
            next_position = puzzle_map[y + offset][x]
            go_y = True
        elif currently_facing == "east" or currently_facing == "west":
            next_position = puzzle_map[y][x + offset]
            go_x = True
    except IndexError:
        # guard can exit the map
        puzzle_map[y] = puzzle_map[y].replace(char, "X")
        return puzzle_map, (x, y), True
    else:
        # move forward or turn 90 degrees right in case of an obstacle
        #obstacle
        if next_position == "#":
            turned_char = turn(char)
            puzzle_map[y] = puzzle_map[y].replace(char, turned_char)
        # move east/west
        elif go_x:
            line_structure = list(current_line)
            char_index = line_structure.index(char)
            line_structure[char_index] = "X"
            line_structure[char_index + offset] = char
            new_line = "".join(line_structure)
            puzzle_map[y] = new_line
        # move north/south
        elif go_y:
            current_line_structure = list(current_line)
            next_line = puzzle_map[y + offset]
            next_lines_structure = list(next_line)
            char_index = current_line_structure.index(char)
            next_lines_structure[char_index] = char
            new_line_string = "".join(next_lines_structure)
            puzzle_map[y + offset] = new_line_string
            puzzle_map[y] = puzzle_map[y].replace(char, "X")

        return puzzle_map, (x, y), False

def parse_map(puzzle_map: list[str]):
    states = list(directions.keys())
    coordinates: list[tuple[int, int]] = []
    # any(state in line for line in puzzle_map for state in states)
    stop = False
    while not stop:
        for line in range(len(puzzle_map)):
            for x in range(len(puzzle_map[line])):
                current_char = puzzle_map[line][x]
                if current_char in states:
                    result = go_forward(puzzle_map, current_char, x, line)
                    puzzle_map = result[0]
                    coordinates.append(result[1])
                    stop = result[2]

    # print("\n".join(puzzle_map))
    # print("\n".join(puzzle_map).count("X"))
    print(len(set(coordinates)))

if __name__ == "__main__":
    filepath = r".\2024\Day 6\input1.txt"
    start = time.time()
    # puzzle_map = test.split("\n")
    
    puzzle_map = format_data(filepath)
    
    parse_map(puzzle_map)
    end = time.time()
    print(f"elapsed: {(end - start):.3f}seconds")
    # print("\n".join(puzzle_map))
    # answer is 4711 (part 1) in 3.7 seconds (previous 14.x-15.x seconds)
