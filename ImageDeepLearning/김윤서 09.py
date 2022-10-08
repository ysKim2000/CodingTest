# 12891번
# DNA 비밀번호

import sys
input = sys.stdin.readline


def solution_9(s, p, string, a, c, g, t):
    answer = 0
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in range(p):
        counts[string[i]] += 1

    if counts['A'] >= a and counts['C'] >= c and counts['G'] >= g and counts['T'] >= t:
        answer += 1

    left = 0
    right = p
    for i in range(s-p):
        counts[string[left]] -= 1
        counts[string[right]] += 1
        if counts['A'] >= a and counts['C'] >= c and counts['G'] >= g and counts['T'] >= t:
            answer += 1
        left += 1
        right += 1

    print(answer)


S, P = map(int, input().split())  # S: 문자열 길이, P: 부분 문자열의 길이
str = list(input())  # 문자열
a, c, g, t = map(int, input().split())
solution_9(S, P, str, a, c, g, t)
