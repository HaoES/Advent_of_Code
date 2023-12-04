with open("input.txt") as f:
    seeds, *blocks = f.read().split("\n\n")
    seeds = list(map(int, seeds.split(":")[1].split()))
    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        for s in seeds:
            for a, b, c in ranges:
                if b <= s <= b + c:
                    new.append(s - b + a)
                    break
            else:
                new.append(s)
        seeds = new
    print(min(seeds))
