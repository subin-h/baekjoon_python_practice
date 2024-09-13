N,K=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
answer1,answer2=0,0
arr1,arr2=[],[]

for i in range(0,N):
    if arr[i][0] == 0:
        arr1.append(arr[i][1])
    else :
        arr2.append(arr[i][1])
        
for j in range(1,7):
    if arr1.count(j)%K==0:
        answer1+=arr1.count(j)//K
    else:
        answer1+=arr1.count(j)//K+1
    if arr2.count(j)%K==0:
        answer2+=arr2.count(j)//K
    else:
        answer2+=arr2.count(j)//K+1
print(answer1+answer2)