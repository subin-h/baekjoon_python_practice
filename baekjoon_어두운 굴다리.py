N=int(input())
M=int(input())
high=[]
x=list(map(int,input().split()))
for i in range(1,len(x)):
    diff =(x[i]-x[i-1])/2
    high.append(diff)
high.append(float(x[0]-0))
high.append(float(N-x[len(x)-1]))

if max(high)//1==max(high):
    print(int(max(high)))
else:
    print(int(max(high))+1)