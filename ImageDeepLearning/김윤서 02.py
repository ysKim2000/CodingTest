import sys
input = sys.stdin.readline

def test():
    N = int(input())
    scores = list(map(int, input().split()))
    M = max(scores)
    result = []

    for i in range(N):
        result.append(scores[i]/M*100)

    print(sum(result) / N)

if __name__ == "__main__":
    test()