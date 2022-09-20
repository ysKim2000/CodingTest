# 1874번
# 스택으로 오름차순 수열 만들기

import sys
from collections import deque 
input = sys.stdin.readline


def solution_11(N):
    stack = deque() # 덱을 stack 처럼 사용
    cnt = 1
    result = [] # +,- 넣을 list
    message = True
    for i in range(N):
        num = int(input())
        while cnt <= num:
            stack.append(cnt) # 덱 오른쪽 추가
            result.append('+')
            cnt += 1
        if stack[-1] == num:
            stack.pop() # 덱 오른쪽 삭제
            result.append('-')
        else:
            message = False
    if message == False:
        print('NO')
    else:
        for i in result:
            print(i)

N = int(input())
solution_11(N)
