N=input()
arr=list(N)
x,y=int(ord(arr[0])-96),int(arr[1])
count=0
q_1=[-1,-2],[-1,+2],[+1,-2],[+1,+2]
q_2=[-2,-1],[-2,+1],[+2,-1],[+2,+1]
for i in q_1:
    if (x+i[0] <1) or (y+i[1] < 1) or (x+i[0] >7) or (y+i[1] > 7):
        continue
    else:
        count+=1
for j in q_2:
    if (x+j[0] <1) or (y+j[1] < 1) or (x+j[0] >7) or (y+j[1] > 7):
        continue
    else:
        count+=1 

print(count)
