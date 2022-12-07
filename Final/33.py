import heapq as hq

N = int(input())
cards = []
for i in range(N):
  hq.heappush(cards, int(input()))

sum = 0
for i in range(N-1):
  count = hq.heappop(cards)+hq.heappop(cards)
  hq.heappush(cards, count)
  sum += count
print(sum)