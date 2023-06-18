score = input()
half = len(score) // 2

first = 0
for i in range(half):
    first += int(score[i])
second = 0
for i in range(half, len(score)):
    second += int(score[i])
if first == second:
    print("LUCKY")
else:
    print("READY")