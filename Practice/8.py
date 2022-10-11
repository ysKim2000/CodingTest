import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0

for i in range(N):
    a = A[:i] + A[i+1:]
    l, r = 0, len(a) - 1

    while l < r:
        s = a[l] + a[r]
        if s == A[i]:
            ans += 1
            break
        elif s < A[i]:
            l += 1
        else:
            r -= 1

print(ans)