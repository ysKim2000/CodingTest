# 2343번: 블루레이 만들기
n, m = map(int, input().split())
lecture = list(map(int, input().split()))

L, R = max(lecture), sum(lecture)
while L <= R:
    mid = (L+R)//2
    temp = mid
    count = 1
    for i in range(n):
        if temp < lecture[i]:
            temp = mid
            count += 1
        temp -= lecture[i]
    if count > m:
        L = mid+1
    else:
        R = mid-1
print(L)