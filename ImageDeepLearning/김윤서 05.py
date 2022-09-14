import sys

def test():
    N, M = map(int, input().split())
    A = list(map(int, sys.stdin.readline().split()))
    arr = [0 for _ in range(M)]

    s = 0
    cnt = 0

    for i in range(N):
        s += A[i]
        res = s % M
        if res == 0:
            cnt += 1

        arr[res] += 1

    for i in range(M):
        cnt += arr[i] * (arr[i] - 1) // 2

    print(cnt)
    

if __name__ == "__main__":
    test()