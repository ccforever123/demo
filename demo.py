import random

p1 = 0
p2 = 1
for i in range(100000):
    last3 = []
    while True:
        x = random.choice([0, 1])
        last3.append(x)
        if len(last3) > 3:
            last3.pop(0)
        if last3 == [1, 0, 0]:
            p1 += 1
            break
        elif last3 == [0, 0, 1]:
            p2 += 1
            break

print('甲（正反反）', p1)
print('乙（反反正）', p2)