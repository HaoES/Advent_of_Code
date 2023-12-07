with open("input.txt") as f:
    lines = []
    for line in f:
        lines.append(line)
    t = int(''.join([i for i in list(lines[0].split(':')[1].strip().split(" ")) if i.isdigit()]))
    d = int(''.join([i for i in list(lines[1].split(':')[1].strip().split(" ")) if i.isdigit()]))

counter = 0
for speed in range(t):
    run = speed * (t - speed)
    if d < run:
        counter += 1
print(counter)
