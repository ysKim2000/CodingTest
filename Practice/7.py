import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

t=set(arr)
print(sum(m-i in t for i in arr)//2)