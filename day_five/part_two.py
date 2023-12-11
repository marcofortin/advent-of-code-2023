from typing import Callable, List, Tuple

Pair = Tuple[int, int]


def get_seed_pairs(line: str) -> List[Pair]:
    seeds = []
    pairs = [int(i) for i in line.split(":")[1].split(" ")[1:]]
    for i in range(0, len(pairs), 2):
        seeds.append((pairs[i], pairs[i + 1]))
    return seeds


def build_mapper(map: List[List[str]]) -> Callable[[List[Pair]], List[Pair]]:
    def mapper(pairs_to_map: List[Pair]) -> List[Pair]:
        mapped_pairs = []

        for range in map:
            dest, source, length = range
            range_start = source
            range_end = source + length
            offset = dest - source
            unmapped_pairs = []

            for pair in pairs_to_map:
                pair_start = pair[0]
                pair_end = pair[0] + pair[1]

                # 1. seed out of this range - (1 unmapped)
                if pair_end < range_start or pair_start > range_end:
                    unmapped_pairs.append((pair_start, pair_end - pair_start))
                    continue

                # 2. seed overlaps entire range - split in 3 pairs
                if pair_start <= range_start and pair_end >= range_end:
                    unmapped_pairs.append(
                        (pair_start, range_start - pair_start)
                    )  # unmapped, start
                    unmapped_pairs.append(
                        (range_end, pair_end - range_end)
                    )  # unmapped, end
                    mapped_pairs.append(
                        (range_start + offset, length)
                    )  # mapped, entire range
                    continue

                # 3. seed overlaps with start - split in 2 pairs (1 mapped, 1 unmapped)
                if pair_start <= range_start:
                    unmapped_pairs.append(
                        (pair_start, range_start - pair_start)
                    )  # unmapped, start
                    mapped_pairs.append(
                        (range_start + offset, pair_end - range_start)
                    )  # mapped, start range
                    continue

                # 4. seed overlaps with end - split in 2 pairs (1 mapped, 1 unmapped)
                if pair_end >= range_end:
                    unmapped_pairs.append(
                        (range_end, pair_end - range_end)
                    )  # unmapped, end
                    mapped_pairs.append(
                        (pair_start + offset, range_end - pair_start)
                    )  # mapped, end range
                    continue

                # 5. seed inside range - (1 mapped)
                mapped_pairs.append(
                    (pair_start + offset, pair_end - pair_start)
                )  # mapped, entire seed
            pairs_to_map = unmapped_pairs

        mapped_pairs.extend(pairs_to_map)  # pairs that couldn't be mapped stay as is

        return [p for p in mapped_pairs if p[1] > 0]  # remove negative ranges

    return mapper


def build_mappers(lines: List[str]) -> List[Callable[[List[Pair]], List[Pair]]]:
    # 1. parse lines into each map
    maps = []
    for line in lines:
        if len(line) == 0:
            continue
        if line[0].isalpha():  # new map
            maps.append([])
            continue
        # continue building map
        maps[-1].append([int(i) for i in line.split(" ")])

    # 2. convert raw map to a function
    return [build_mapper(map) for map in maps]


def get_min_location_number(
    seed_pair: Tuple[int, int], mappers: List[Callable[[List[Pair]], List[Pair]]]
) -> int:
    pairs_to_map = [seed_pair]
    for mapper in mappers:
        pairs_to_map = mapper(pairs_to_map)
    return min(
        [p[0] for p in pairs_to_map]
    )  # at this point, pairs to map are locations, grab the min location.


def find_lowest_location_number() -> str:
    res = float("inf")
    with open("input.txt") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
        seed_pairs = get_seed_pairs(lines[0])
        mappers = build_mappers(lines[1:])
        for seed_pair in seed_pairs:
            res = min(res, get_min_location_number(seed_pair, mappers))
    return res


if __name__ == "__main__":
    print(find_lowest_location_number())
