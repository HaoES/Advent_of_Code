final = 0
with open("input.txt") as f:
    for line in f:
        power = 1
        total = {"red": 0, "blue": 0, "green": 0}
        games = line.split(":")[1][:-1]
        rounds = games.split(";")
        rounds = [r.strip() for r in rounds]
        # print(rounds)
        for r in rounds:
            plays = r.strip().split(",")
            for p in plays:
                update = p.strip().split(" ")
                total[update[-1]] = max(int(update[0]), int(total[update[-1]]))
        for v in total.values():
            power *= v
        final += power
print(final)
