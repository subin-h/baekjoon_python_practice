import sys
N,M,K=map(int,input().split())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort(reverse=True)
first_count=K*(M//(K+1))+M%(K+1)
answer=arr[0]*first_count+arr[1]*(M-first_count)
print(answer)