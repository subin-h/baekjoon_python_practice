import sys
N=int(input())
arr=[]
for i in range(N):
    A,B=sys.stdin.readline().split()
    C=int(A)
    arr.append([C,B])
answer=sorted(arr,key=lambda x:x[0])
for x,y in answer:
    print(x,y)