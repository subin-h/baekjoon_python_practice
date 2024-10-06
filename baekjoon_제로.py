K=int(input())
arr=[]
for i in range(K):
    N=int(input())
    arr.append(N)
    if N==0:
        arr.pop()
        arr.pop()
print(sum(arr))