import random
import json

n = random.randint(1, 6)
nums = [random.randint(0, 12) for _ in range(n)]

# Sometimes force some edge cases
if random.random() < 0.3:
    # include a zero
    nums[random.randint(0, n - 1)] = 0
if random.random() < 0.3:
    # duplicates
    v = random.randint(1, 12)
    nums[random.randint(0, n - 1)] = v
    if n >= 2:
        nums[random.randint(0, n - 1)] = v

k = random.randint(-10, 10)
limit = random.randint(1, 50)

print(str(nums))
print(k)
print(limit)
