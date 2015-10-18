__author__ = 'GCA'
# Date: 2015/10/19
n = int(input())
a = n ** 0.5 + 1
d = 2
A = 1
while d <= a:
    if n % d == 0:
        n //= d
        if A % d != 0:
            A *= d
    else:
        d += 1
if n > 1:
    A *= n
print(A)
