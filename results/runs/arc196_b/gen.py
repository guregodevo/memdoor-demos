import random

T = random.randint(1, 3)
print(T)
for _ in range(T):
    H = random.randint(2, 3)
    W = random.randint(2, 3)
    print(H, W)
    for i in range(H):
        row = ''.join(random.choice('AB') for _ in range(W))
        print(row)
