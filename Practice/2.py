import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))
print(sum(scores)*(100/max(scores))/N)