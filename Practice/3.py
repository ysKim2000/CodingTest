import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int,input().split()))

for i in range(n-1):
    num[i+1] += num[i]
num = [0] + num

for i in range(m):
    a, b = map(int,input().split())
    print(num[b] - num[a-1])