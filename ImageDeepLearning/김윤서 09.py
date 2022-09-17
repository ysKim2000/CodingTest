# 12891번
# DNA 비밀번호

import sys
import collections
input = sys.stdin.readline

S, P = map(int, input().split()) # S: 문자열 길이, P: 부분 문자열의 길이
str = list(input().split()) # 문자열
cnt = list(input().split(' ')) # 부분 문자열의 포함되어야 할 갯수


def solution_9(S, P, str, cnt):
    DNA = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
    }
    
    result = []
    window = collections.deque()

    for i, v in enumerate(S):
        window.append(v)



solution_9(S, P, str, cnt)
