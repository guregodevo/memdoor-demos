import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    A = tuple(int(data[i + 1]) for i in range(n))

    def dp(seq):
        if len(seq) <= 1:
            return 0
        best = 0
        for i in range(len(seq) - 1):
            score = abs(seq[i] - seq[i + 1])
            new_seq = seq[:i] + seq[i + 2:]
            val = score + dp(new_seq)
            if val > best:
                best = val
        return best

    print(dp(A))

main()
