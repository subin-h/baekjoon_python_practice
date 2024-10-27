N=int(input())
storage=list(map(int,input().split()))
d= [0] * (N+1)
d[1]=storage[0]
d[2]=max(storage[0],storage[1])
for i in range(3,N+1):
    d[i]=max(d[i-1],storage[i-1]+d[i-2])
print(d[N])
