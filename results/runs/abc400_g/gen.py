import random

def main():
    T = random.randint(1, 3)
    lines = [str(T)]
    for _ in range(T):
        N = random.randint(2, 8)
        K = random.randint(1, N // 2)
        lines.append(f"{N} {K}")
        for _ in range(N):
            x = random.randint(0, 20)
            y = random.randint(0, 20)
            z = random.randint(0, 20)
            lines.append(f"{x} {y} {z}")
    print('\n'.join(lines))

main()
