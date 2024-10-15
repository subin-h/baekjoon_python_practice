import sys
N,K = map(int,input().split())
A=sys.stdin.readline().split()
B=sys.stdin.readline().split()
A_sorted=sorted(A)
B_sorted=sorted(B, reverse=True)
for i in range(K):
    if A_sorted[i] >= B_sorted[i]:
        break
    A_sorted[i], B_sorted[i] = B_sorted[i], A_sorted[i]
print(sum(map(int,A_sorted)))