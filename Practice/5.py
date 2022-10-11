import sys
input = sys.stdin.readline

N, M = map(int,input().split())
num = list(map(int,input().split()))
r, t, ans = [0]*M, 0, 0
for n in range(N):
    t = (t + num[n])%M
    r[t] += 1

r[0] += 1
for v in r:
    ans += (v-1)*v//2
print(ans)