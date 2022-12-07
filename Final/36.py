# 1541번: 최솟값을 만드는 괄호 배치 찾기
n=[sum(map(int,x.split("+"))) for x in input().split("-")]
print(n[0]-sum(n[1:]))