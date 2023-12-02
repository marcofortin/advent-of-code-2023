DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_digit(s: str) -> str:
    """
    if the given string starts with a digit, returns the digit otherwise returns an empty string.

    a digit can either be of numerical character (e.g. '1') or a string (e.g. 'one')
    """
    if s[0].isnumeric():
        return s[0]
    for digit_str, digit_val in DIGITS.items():
        if s.startswith(digit_str):
            return digit_val
    return ""


def get_calibration_value(line: str) -> int:
    first_digit = last_digit = -1
    for i in range(len(line)):
        maybe_digit = get_digit(line[i:])
        if not maybe_digit:
            continue

        if first_digit == -1:  # first digit we see
            first_digit = maybe_digit
            last_digit = maybe_digit
        else:
            last_digit = maybe_digit

    return int(f"{first_digit}{last_digit}")


def sum_calibration_values() -> int:
    with open("calibration_document.txt") as f:
        res = 0
        for line in f:
            res += get_calibration_value(line)
        return res


if __name__ == "__main__":
    print(sum_calibration_values())
