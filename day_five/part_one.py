from typing import List


def get_seeds(line: str) -> List[int]:
    return [int(seed) for seed in line.split(":")[1].split(" ")[1:]]


def build_maps(lines: List[str]) -> List[List[List[int]]]:
    maps = []
    for line in lines:
        if len(line) == 0:
            continue
        if line[0].isalpha():  # new map
            maps.append([])
            continue
        # continue building map
        maps[-1].append([int(i) for i in line.split(" ")])
    return maps


def get_location_number(seed: int, maps: List[List[List[int]]]) -> int:
    element_to_map = seed
    for map in maps:
        for range in map:
            dest, source, length = range
            if (element_to_map < source) or (element_to_map > source + length):
                continue  # not in this range
            element_to_map = element_to_map + (dest - source)
            break  # moving on to new map
    return element_to_map  # location


def find_lowest_location_number() -> str:
    res = float("inf")
    with open("input.txt") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
        seeds = get_seeds(lines[0])
        maps = build_maps(lines[1:])
        for seed in seeds:
            res = min(res, get_location_number(seed, maps))
    return res


if __name__ == "__main__":
    print(find_lowest_location_number())
