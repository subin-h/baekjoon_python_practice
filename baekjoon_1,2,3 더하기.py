import sys

T = int(input())
input = sys.stdin.readline
d = [0] * 11

d[1],d[2],d[3] = 1,2,4

for i in range(4,11):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for _ in range(T):
    K = int(input())
    print(d[K])