# 1940번
# 주몽

import sys
input = sys.stdin.readline


def solve():
    N = int(input()) # 재료의 갯수
    M = int(input()) # 갑옷을 만드는데 필요한 수
    arr = sorted(list(map(int, input().split()))) # 고유한 번호

    cnt = 0
    start = 0
    end = N - 1

    while start != end:
        if arr[start] + arr[end] == M:
            end -= 1
            cnt += 1
        elif arr[start] + arr[end] < M:
            start += 1
        elif arr[start] + arr[end] > M:
            end -= 1

    print(cnt)

if __name__ == "__main__":
    solve()