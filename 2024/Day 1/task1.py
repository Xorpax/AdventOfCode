input_file = r"2024\Day 1\input1.txt"

# compile separate lists of location IDs
with open(input_file, "r") as inp:
    list_of_locations: list[str] = inp.readlines()
    locations_left: list[int] = []
    locations_right: list[int] = []
    for row in list_of_locations:
        l_location, r_location = int(row.split()[0]), int(row.split()[1])
        locations_left.append(l_location), locations_right.append(r_location)

total_distance: int = 0

for distance in range(len(locations_left)):
    l_min: int = min(locations_left)
    l_min_pos: int = locations_left.index(l_min)
    r_min: int = min(locations_right)
    r_min_pos: int = locations_right.index(r_min)
    dist = abs(l_min - r_min)
    locations_left[l_min_pos] = max(locations_left) + 1
    locations_right[r_min_pos] = max(locations_right) + 1
    total_distance += dist

print(total_distance)
# answer is 3569916
