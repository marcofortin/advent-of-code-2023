from typing import List, Set, Tuple


def get_adjacent_part_numbers(
    row_idx: int, col_idx: int, lines: List[str], seen: Set[Tuple[int, int]]
) -> int:
    if (
        row_idx == -1
        or row_idx == len(lines)
        or col_idx == -1
        or col_idx == len(lines[0])
    ):
        return 0  # outside grid

    if not lines[row_idx][col_idx].isnumeric():
        return 0  # not a number

    if (row_idx, col_idx) in seen:
        return 0  # already accounted for this number

    res = lines[row_idx][col_idx]

    for i in range(col_idx - 1, -1, -1):  # prefix with digits to left
        if not lines[row_idx][i].isnumeric():
            break  # not a number, stop looking left

        seen.add((row_idx, i))
        res = (lines[row_idx][i]) + res

    for i in range(col_idx + 1, len(lines[row_idx])):  # postfix with digits to right
        if not lines[row_idx][i].isnumeric():
            break  # not a number, stop looking left

        seen.add((row_idx, i))
        res += lines[row_idx][i]

    return int(res)


def sum_gear_ratios() -> int:
    res = 0

    with open("input.txt") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

        for row_idx in range(len(lines)):
            for col_idx in range(len(lines[row_idx])):
                char = lines[row_idx][col_idx]
                if char != "*":
                    continue

                seen = set()
                adjacent_part_numbers = [
                    get_adjacent_part_numbers(
                        row_idx - 1, col_idx - 1, lines, seen
                    ),  # top left
                    get_adjacent_part_numbers(row_idx - 1, col_idx, lines, seen),  # top
                    get_adjacent_part_numbers(
                        row_idx, col_idx - 1, lines, seen
                    ),  # left
                    get_adjacent_part_numbers(
                        row_idx - 1, col_idx + 1, lines, seen
                    ),  # top right
                    get_adjacent_part_numbers(
                        row_idx, col_idx + 1, lines, seen
                    ),  # right
                    get_adjacent_part_numbers(
                        row_idx + 1, col_idx - 1, lines, seen
                    ),  # bottom left
                    get_adjacent_part_numbers(
                        row_idx + 1, col_idx, lines, seen
                    ),  # bottom
                    get_adjacent_part_numbers(
                        row_idx + 1, col_idx + 1, lines, seen
                    ),  # bottom right
                ]

                adjacent_part_numbers = [
                    num for num in adjacent_part_numbers if num > 0
                ]
                if len(adjacent_part_numbers) != 2:  # not a gear
                    continue

                res += (
                    adjacent_part_numbers[0] * adjacent_part_numbers[1]
                )  # gear's ratio

        return res


if __name__ == "__main__":
    print(sum_gear_ratios())
