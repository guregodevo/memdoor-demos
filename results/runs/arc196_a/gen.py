import random

def main():
    N = random.randint(2, 8)
    style = random.choice(['normal', 'small', 'same', 'extreme'])
    if style == 'normal':
        A = [random.randint(1, 50) for _ in range(N)]
    elif style == 'small':
        A = [random.randint(1, 5) for _ in range(N)]
    elif style == 'same':
        v = random.randint(1, 100)
        A = [v] * N
    else:
        A = [random.choice([1, 10**9, random.randint(1, 10**9)]) for _ in range(N)]
    print(N)
    print(' '.join(map(str, A)))

main()
