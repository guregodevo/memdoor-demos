import random
import json

n = random.randint(1, 5)
nums = [random.randint(1, 1000) for _ in range(n)]
cost = [random.randint(1, 1000) for _ in range(n)]
k = random.randint(1, 1000)

print(json.dumps(nums))
print(json.dumps(cost))
print(k)
