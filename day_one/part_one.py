def get_calibration_value(line: str) -> int:
    first_digit = last_digit = -1
    for char in line:
        if char.isnumeric():
            if first_digit == -1:  # first digit we see
                first_digit = char
                last_digit = char
            else:
                last_digit = char

    return int(f"{first_digit}{last_digit}")


def sum_calibration_values() -> int:
    with open("input.txt") as f:
        res = 0
        for line in f:
            res += get_calibration_value(line)
        return res


if __name__ == "__main__":
    print(sum_calibration_values())
