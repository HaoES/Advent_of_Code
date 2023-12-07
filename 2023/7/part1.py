hands = []
bids = []
with open("input.txt") as f:
    for line in f:
        hands.append(line.split(" ")[0])
        bids.append(int(line.split(" ")[1]))


def handeval(hand):
    if len(set(hand)) == 1:
        return 1
    if len(set(hand)) == 2:
        if hand.count(hand[0]) == 1 or hand.count(hand[1]) == 4:
            return 2
        else:
            return 3
    if len(set(hand)) == 3:
        if (
            hand.count(hand[0]) == 3
            or hand.count(hand[1]) == 3
            or hand.count(hand[2]) == 3
        ):
            return 4
        else:
            return 5
    if len(set(hand)) == 4:
        return 6
    if len(set(hand)) == 5:
        return 7


def alpheval(hand):
    alphabet = "AKQJT98765432"
    score = [None] * 6
    for i, s in enumerate(hand):
        score[i + 1] = alphabet.index(s)
    return score


hand_score = [handeval(h) for h in hands]
hand_alpha = [alpheval(h) for h in hands]

for hs, ha in zip(hand_score, hand_alpha):
    ha[0] = hs

d = {bid: score for bid, score in zip(bids, hand_alpha)}
final = dict(
    sorted(
        d.items(),
        key=lambda x: (x[1][0], x[1][1], x[1][2], x[1][3], x[1][4]),
        reverse=True,
    )
)
tot = 0
for k, i in zip(final.keys(), range(1, len(final) + 1)):
    tot += k * i
print(tot)
