# 2018번
# 연속된 자연수의 합

import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    cnt = 0
    sum = 0
    start = 0
    end = 0
    while end <= N:
        if sum < N:
            end += 1
            sum += end
        elif sum > N:
            sum -= start
            start += 1
        else:
            cnt += 1
            end += 1
            sum += end
    print(cnt)


if __name__ == "__main__":
    solve()