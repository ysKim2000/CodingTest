# 12891번
# DNA 비밀번호

import sys
input = sys.stdin.readline


def solution_9(S, P, str, num):
    DNA = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
    }
    
    DNA_cnt = {
        'A': num[0],
        'C': num[1],
        'G': num[2],
        'T': num[3]
    }

    cnt = 0
    for i in range(S - P + 1):
        flag = True

        if i == 0:
            for j in range(P):
                DNA[str[j]] += 1
        else:
            DNA[str[i+P-1]] += 1
            DNA[str[i-1]] -= 1

        for i in ('A', 'C', 'G', 'T'):
            if DNA[i] < DNA_cnt[i]:
                flag = False
                break

        if flag:
            cnt += 1
    print(cnt)


S, P = map(int, input().split())  # S: 문자열 길이, P: 부분 문자열의 길이
str = list(input())  # 문자열
num = list(map(int, input().split()))
solution_9(S, P, str, num)
