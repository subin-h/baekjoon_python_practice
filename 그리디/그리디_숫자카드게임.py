N,M=map(int,input().split())
answer=0
arr_=[list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    max_arr=min(arr_[i])
    if answer < max_arr:
        answer=max_arr
print(answer)