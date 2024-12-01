input_file = r"2024\Day 1\Task 2\input.txt"

# compile separate lists of location IDs
with open(input_file, "r") as inp:
    list_of_locations: list[str] = inp.readlines()
    locations_left: list[int] = []
    locations_right: list[int] = []
    for row in list_of_locations:
        l_location, r_location = int(row.split()[0]), int(row.split()[1])
        locations_left.append(l_location), locations_right.append(r_location)

similarity_score: int = 0

for num in locations_left:
    r_count = locations_right.count(num)
    similarity_score += num * r_count

print(similarity_score)