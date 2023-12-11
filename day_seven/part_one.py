import functools
from typing import List, Tuple


FACE_CARD_VALUE = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
}


def build_hands(lines: List[str]) -> List[Tuple[str, int]]:
    res = []
    for line in lines:
        (
            hand,
            bid,
        ) = line.split(" ")
        res.append((hand, int(bid)))
    return res


def get_card_value(card: str) -> int:
    if card.isnumeric():
        return int(card)
    return FACE_CARD_VALUE[card]


def get_hand_value(hand: Tuple[str, int]) -> int:
    seen = {}
    for card in hand[0]:
        if card not in seen:
            seen[card] = 0
        seen[card] += 1

    values = list(seen.values())
    values.sort(reverse=True)
    if values == [5]:  # five of a kind
        return 6
    if values == [4, 1]:  # four of a kind
        return 5
    if values == [3, 2]:  # full house
        return 4
    if values == [3, 1, 1]:  # three of a kind
        return 3
    if values == [2, 2, 1]:  # two pair
        return 2
    if values == [2, 1, 1, 1]:  # one pair
        return 1
    return 0  # high card


def compare_hand(hand_one: Tuple[str, int], hand_two: Tuple[str, int]) -> int:
    hand_one_value = get_hand_value(hand_one)
    hand_two_value = get_hand_value(hand_two)
    if hand_one_value < hand_two_value:
        return -1
    if hand_one_value > hand_two_value:
        return 1

    for card_hand_one, card_hand_two in zip(hand_one[0], hand_two[0]):
        card_hand_one_value = get_card_value(card_hand_one)
        card_hand_two_value = get_card_value(card_hand_two)
        if card_hand_one_value < card_hand_two_value:
            return -1
        if card_hand_one_value > card_hand_two_value:
            return 1


def find_total_winnings() -> int:
    res = 0
    with open("input.txt") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
        hands = build_hands(lines)
        hands.sort(key=functools.cmp_to_key(compare_hand))
        for rank, hand in enumerate(hands):
            res += hand[1] * (rank + 1)

    return res


if __name__ == "__main__":
    print(find_total_winnings())
