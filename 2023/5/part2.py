with open("input.txt") as f:
    seeds, *blocks = f.read().split("\n\n")
    seeds = list(map(int, seeds.split(":")[1].split()))
    total_seeds = []
    for i in range(0, len(seeds), 2):
        total_seeds.append((seeds[i], seeds[i] + seeds[i + 1]))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        while len(total_seeds) > 0:
            start, end = total_seeds.pop()
            for a, b, c in ranges:
                os = max(b, start)
                oe = min(end, b + c)
                if os < oe:
                    new.append((os - b + a, oe - b + a))
                    if os > start:
                        total_seeds.append((start, os))
                    if end > oe:
                        total_seeds.append((oe, end))
                    break
            else:
                new.append((start, end))
        total_seeds = new
print(sorted(total_seeds)[0][0])
