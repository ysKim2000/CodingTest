import sys
input = sys.stdin.readline

def test():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    result = [0]
    x = 0

    for i in arr:
        x += i
        result.append(x)

    for i in range(M):
        a, b = map(int, input().split())
        print(result[b] - result[a-1])

if __name__ == "__main__":
    test()