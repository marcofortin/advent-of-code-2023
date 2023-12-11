from typing import Tuple


def build_race(time_line: str, distance_line: str) -> Tuple[int, int]:
    return int(time_line.split(":")[1].replace(" ", "")), int(
        distance_line.split(":")[1].replace(" ", "")
    )


def get_number_ways_to_beat_record(race: Tuple[int, int]) -> int:
    res = 0
    time, distance = race
    for i in range(time):
        if i * (time - i) > distance:
            res += 1
    return res


def find_number_ways_to_beat_record() -> int:
    with open("input.txt") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
        race = build_race(lines[0], lines[1])
        return get_number_ways_to_beat_record(race)


if __name__ == "__main__":
    print(find_number_ways_to_beat_record())
