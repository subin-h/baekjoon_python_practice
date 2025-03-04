import sys
N,M=map(int,input().split())
bill=[]
for _ in range(N):
    bill.append(int(sys.stdin.readline()))
bill.sort(reverse=True)
d = [10001] * (M+1)
d[0]=0
for i in range(N):
    for j in range(bill[i], M+1):
        if d[j-bill[i]] != 10001:
            d[j] = min(d[j], d[j-bill[i]]+1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])