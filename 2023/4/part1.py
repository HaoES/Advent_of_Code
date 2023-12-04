total = 0
with open("input.txt") as f:
    for line in f:
        winning = [
            i for i in line.split(":")[1].split("|")[0].strip().split(" ") if i != ""
        ]
        numbers = [
            i for i in line.split(":")[1].split("|")[1].strip().split(" ") if i != ""
        ]
        score = 0
        w_numbers = set(numbers).intersection(set(winning))
        if len(w_numbers) == 0:
            continue
        else:
            total += 2 ** (len(w_numbers) - 1)
print(total)
