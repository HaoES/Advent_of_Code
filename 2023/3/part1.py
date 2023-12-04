digits = []
locations = set()
with open("input.txt") as f:
    grid = [list(line.rstrip("\n")) for line in f]
for r, row in enumerate(grid):
    for c, element in enumerate(row):
        if element.isdigit() or element == ".":
            continue
        for x in [r - 1, r, r + 1]:
            for y in [c - 1, c, c + 1]:
                if (
                    x < 0
                    or x >= len(grid)
                    or y < 0
                    or y >= len(grid[x])
                    or not grid[x][y].isdigit()
                ):
                    continue
                while y > 0 and grid[x][y - 1].isdigit():
                    y -= 1
                locations.add((x, y))

for x, y in locations:
    digit = ""
    while y < len(grid[x]) and grid[x][y].isdigit():
        digit += grid[x][y]
        y += 1
    digits.append(int(digit))
print(sum(digits))
