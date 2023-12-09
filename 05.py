from aocd import data
from aocd import submit
import re

parts = data.split(':')
numbers = map(lambda s: list(map(int, re.findall(r'\d+', s))), parts)
numbers = list(filter(lambda e: len(e) > 0, numbers))
seeds = list(numbers[0])
maps = map(lambda m: sorted(zip(* [iter(m)] * 3), key=lambda e: e[1]), numbers[1:])
maps = list(map(lambda m: list(map(lambda e: (e[0] - e[1], e[1], e[1] + e[2]), m)), maps))

def map_seed(seed):
    for m in maps:
        for ofs, m_begin, m_end in m:
            if seed >= m_begin and seed < m_end:
                seed += ofs
                break

    return seed

submit(min(map(map_seed, seeds)), part='a')

def map_ranges(seed_ranges):
    for m in maps:
        mapped = []
        for begin, end in seed_ranges:
            for ofs, m_begin, m_end in m:
                if end <= m_begin:
                    mapped.append((begin, end))
                    begin = end
                    break

                if begin < m_begin:
                    mapped.append((begin, m_begin))
                    begin = m_begin

                if end <= m_end:
                    mapped.append((begin + ofs, end + ofs))
                    begin = end
                    break

                if begin < m_end:
                    mapped.append((begin + ofs, m_end + ofs))
                    begin = m_end

            if begin < end:
                mapped.append((begin, end))

        seed_ranges = mapped

    return seed_ranges

seed_ranges = list(map(lambda e:(e[0], e[0] + e[1]), zip(* [iter(seeds)] * 2)))

submit(min(map(lambda e: e[0], map_ranges(seed_ranges))), part='b')
