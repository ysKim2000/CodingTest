import sys
input = sys.stdin.readline
n,m = map(int,input().split())
s = input()
a,c,g,t = map(int,input().split())
cnt = 0
d = {'A':0,'C':0,'G':0,'T':0}
for i in s[:m]:
    d[i] += 1
if d['A'] >= a and d['C'] >=c and d['G']>=g and d['T'] >= t:
    cnt += 1
for i in range(1,n-m+1):
    d[s[i-1]] -= 1
    d[s[m+i-1]] += 1
    if d['A'] >= a and d['C'] >=c and d['G']>=g and d['T'] >= t:
        cnt += 1
print(cnt)