with open("input.txt") as f:
    lines = []
    for line in f:
        lines.append(line)
    time = [
        int(i) for i in list(lines[0].split(":")[1].strip().split(" ")) if i.isdigit()
    ]
    distance = [
        int(i) for i in list(lines[1].split(":")[1].strip().split(" ")) if i.isdigit()
    ]

ways = []
for t, d in zip(time, distance):
    counter = 0
    for speed in range(t):
        run = speed * (t - speed)
        if d < run:
            counter += 1
    ways.append(counter)

product = 1
for w in ways:
    print(w)
    product = product * w
print(product)
