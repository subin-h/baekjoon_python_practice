import sys
N=int(input())
arr=[]
for _ in range(N):
    number=sys.stdin.readline()
    arr.append(number.strip())
answer=sorted(arr,reverse=True)
print(' '.join(answer))
