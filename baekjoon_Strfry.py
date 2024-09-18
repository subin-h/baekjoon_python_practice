N=int(input())
k=[]
for i in range(0,N):
    N1,N2=input().split()
    num1=sorted(N1)
    num2=sorted(N2)
    if num1 == num2:
        k.append(1)
    else:
        k.append(0)
for j in k:
    if j==1:
        print("Possible")
    else:
        print("Impossible")


    
