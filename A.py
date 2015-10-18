__author__ = 'GCA'
# Date: 2015/10/18

n = int(input())
minp = 200
total = 0
for i in range(n):
    ai, pi = list(map(int, input().split()))
    if pi < minp:
        minp = pi
    total += minp * ai
print(total)
