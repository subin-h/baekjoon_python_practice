import sys # 빠른 입력 라이브러리
N=int(input())
arr=[]
for _ in range(N):
    arr+=list(map(int, sys.stdin.readline().split()))
print("\n".join((map(str,sorted(arr)))))