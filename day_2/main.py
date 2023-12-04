import os


def is_valid_roll(roll_summary):
    limit_dict = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    rolls = roll_summary.split(",")
    for cube in rolls:
        cube_details = cube.strip().split(" ")
        if int(cube_details[0]) > limit_dict[cube_details[1]]:
            return False

    return True


def get_power(vals):
    power = 1

    for key, value in vals.items():
        power *= value
    return power


def find_min_set(roll_summary):
    min_vals = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for rolls in roll_summary:
        cubes = rolls.split(",")

        for cube in cubes:
            cube_details = cube.strip().split(" ")
            cd_val = int(cube_details[0])

            if cd_val > min_vals[cube_details[1]]:
                min_vals[cube_details[1]] = cd_val

    return get_power(min_vals)


def getValidGames(line):
    game = line.split(":")
    rolls = game[1].split(";")
    min_set = find_min_set(rolls)

    for roll in rolls:
        if not is_valid_roll(roll):
            return 0

    return int(game[0].replace("Game ", ""))


def getPowerOfSets(line):
    game = line.split(":")
    rolls = game[1].split(";")
    return find_min_set(rolls)


input_file_loc = f"{os.getcwd()}/day_2/input.txt"

with open(input_file_loc, "r") as input:
    data = input.readlines()
    sum_of_valid_games = sum(list(map(getValidGames, data)))
    power_of_sets = sum(list(map(getPowerOfSets, data)))

    print(
        f"Sum of Valid Game Ids: {sum_of_valid_games}; Power of Sets: {power_of_sets}")
    input.close()
