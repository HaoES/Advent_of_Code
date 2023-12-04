from collections import defaultdict

cards = {}
total = defaultdict()
line_number = 0
with open("input.txt") as f:
    for line in f:
        line_number += 1
        winning = [
            i for i in line.split(":")[1].split("|")[0].strip().split(" ") if i != ""
        ]
        numbers = [
            i for i in line.split(":")[1].split("|")[1].strip().split(" ") if i != ""
        ]
        score = 0
        w_numbers = set(numbers).intersection(set(winning))
        total[line_number] = len(w_numbers)
        cards[line_number] = 1

    for k, v in total.items():
        for i in range(k + 1, k + v + 1):
            if i > len(cards):
                break
            cards[i] += 1 * cards[k]

print(sum(cards.values()))
