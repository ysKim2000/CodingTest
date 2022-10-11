import sys
input = sys.stdin.readline

n = int(input())
values = []
for _ in range(n):
    values.append(int(input()))
stack = []
ans = []
last = 1

for v in values:
    while last <= v:
        stack.append(last)
        ans.append('+')
        last += 1
    if stack[-1] != v:
        print('NO')
        exit(0)
    stack.pop()
    ans.append('-')

print('\n'.join(ans))