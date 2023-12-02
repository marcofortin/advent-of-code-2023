bag = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_possible(game_section: str) -> bool:
    for game_info in game_section.split(";"):
        for color_info in game_info.split(","):
            num, color = color_info.split(" ")[1:]
            if int(num) > bag[color]:
                return False
    return True


def parse_game_id(id_section: str) -> int:
    return int(id_section.split(" ")[1])


def sum_possible_game_ids() -> int:
    with open("input.txt") as f:
        res = 0
        for line in f:
            id_section, game_section = line.rstrip("\n").split(":")
            game_id = parse_game_id(id_section)
            if is_possible(game_section):
                res += game_id
        return res


if __name__ == "__main__":
    print(sum_possible_game_ids())
