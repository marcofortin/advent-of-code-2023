def get_power_min_set_cubes(game_section: str) -> int:
    min_set_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for game_info in game_section.split(";"):
        for color_info in game_info.split(","):
            num, color = color_info.split(" ")[1:]
            min_set_cubes[color] = max(min_set_cubes[color], int(num))
    res = 1
    for min_val in min_set_cubes.values():
        res *= min_val
    return res


def sum_possible_game_ids() -> int:
    with open("input.txt") as f:
        res = 0
        for line in f:
            game_section = line.rstrip("\n").split(":")[1]
            res += get_power_min_set_cubes(game_section)
        return res


if __name__ == "__main__":
    print(sum_possible_game_ids())
