valid_lines = 0
line_number = 0
with open("input.txt") as f:
    for line in f:
        valid = True
        line_number += 1
        games = line.split(":")[1][:-1]
        rounds = games.split(";")
        rounds = [r.strip() for r in rounds]
        # print(rounds)
        for r in rounds:
            total = {"red": 0, "blue": 0, "green": 0}
            plays = r.strip().split(",")
            for p in plays:
                update = p.strip().split(" ")
                total[update[-1]] += int(update[0])
            if total["red"] > 12 or total["blue"] > 14 or total["green"] > 13:
                valid = False
        if valid:
            valid_lines += line_number
print(valid_lines)
