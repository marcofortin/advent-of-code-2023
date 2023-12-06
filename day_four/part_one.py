from typing import List


def get_numbers(s: str) -> List[int]:
    return [int(n) for n in s.split(" ") if n]


def get_card_value(line: str) -> int:
    res = 0
    line = line.split(":")[1]
    winning_numbers, card_numbers = line.split("|")
    winning_numbers = get_numbers(winning_numbers)
    card_numbers = get_numbers(card_numbers)

    for num in card_numbers:
        if num in winning_numbers:
            if res == 0:
                res = 1
            else:
                res *= 2

    return res


def sum_card_points() -> int:
    res = 0

    with open("input.txt") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

        for line in lines:
            res += get_card_value(line)

        return res


if __name__ == "__main__":
    print(sum_card_points())
