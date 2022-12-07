# 1920번: 원하는 정수 찾기
from sys import stdin
input = stdin.readline

n = input()
N = set(input().split())
m = input()
M = input().split()

for l in M:
    print('1') if l in N else print('0')