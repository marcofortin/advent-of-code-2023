from typing import List


def get_numbers(s: str) -> List[int]:
    return [int(n) for n in s.split(" ") if n]


def get_number_cards_won(line: str) -> int:
    res = 0
    line = line.split(":")[1]
    winning_numbers, card_numbers = line.split("|")
    winning_numbers = get_numbers(winning_numbers)
    card_numbers = get_numbers(card_numbers)

    for num in card_numbers:
        if num in winning_numbers:
            res += 1

    return res


def sum_card_points() -> int:
    with open("input.txt") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

        cards = {i: 1 for i in range(1, len(lines) + 1)}
        for curr_card_idx, line in enumerate(lines):
            curr_card_num = curr_card_idx + 1
            number_cards_won = get_number_cards_won(line)
            for i in range(1, number_cards_won + 1):
                cards[curr_card_num + i] += cards[curr_card_num]

        return sum(cards.values())


if __name__ == "__main__":
    print(sum_card_points())
