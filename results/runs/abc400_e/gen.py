import random

Q = random.randint(1, 5)
queries = []
for _ in range(Q):
    A = random.randint(36, 5000)
    queries.append(A)

print(Q)
for q in queries:
    print(q)
