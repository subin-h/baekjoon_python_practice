count=1
brr=[]
arr=list(map(int,input().split()))
start_c=list(map(int,input().split()))
field=[list(map(int,input().split())) for _ in range(arr[1])]
direct={0:[0,-1], 1:[1,0],2:[0,1],3:[1,0]}
x=start_c[0]
y=start_c[1]
z=start_c[2] #방향
while True:
    if (field[x+1][y]==1) and (field[x-1][y]==1) and (field[x][y+1]==1) and (field[x][y-1]==1):
        break
    field[x][y]=1
    brr=direct[z]
    a,b=list(brr)
    z=(z+3)%4
    if field[x+a][y+b] == 1:
        continue
    else:
        field[x+a][y+b]=1
        count+=1
        x+=a
        y+=b
print(count)