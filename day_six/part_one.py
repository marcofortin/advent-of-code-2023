from typing import List, Tuple


def get_elements(line: str) -> List[int]:
    return [int(e) for e in line.split(":")[1].split()]


def build_races(time_line: str, distance_line: str) -> List[Tuple[int, int]]:
    return [
        (time, distance)
        for time, distance in zip(get_elements(time_line), get_elements(distance_line))
    ]


def get_number_ways_to_beat_record(race: Tuple[int, int]) -> int:
    res = 0
    time, distance = race
    for i in range(time):
        if i * (time - i) > distance:
            res += 1
    return res


def find_number_ways_to_beat_record() -> int:
    res = 1
    with open("input.txt") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
        races = build_races(lines[0], lines[1])
        for race in races:
            res *= get_number_ways_to_beat_record(race)
    return res


if __name__ == "__main__":
    print(find_number_ways_to_beat_record())
