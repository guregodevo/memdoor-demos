import random

N = random.randint(1, 5)
chars = ['W'] * N + ['B'] * N
random.shuffle(chars)
S = ''.join(chars)

print(N)
print(S)
