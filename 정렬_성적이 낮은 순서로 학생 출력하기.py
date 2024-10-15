N=int(input())
arr=[]
for _ in range(N):
    arr.append(input().split())
sorted_arr=sorted(arr,key=lambda x: x[1])
name=[row[0] for row in sorted_arr]
print(' '.join(name))