import random
import json

k = random.randint(1, 3)
x = random.randint(2, 3)
min_n = max(2, k * x)
n = random.randint(min_n, min_n + 3)

nums = [random.randint(-5, 5) for _ in range(n)]

print(json.dumps(nums))
print(x)
print(k)
