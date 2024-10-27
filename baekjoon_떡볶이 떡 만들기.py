N,M=map(int,input().split())
N_list=sorted(map(int,input().split()))
result=0
def binary_search(start, end, list):
    global result
    while(start <= end):
        total=0
        mid=(start+end)//2
        for i in list:
            if i > mid:
                total+=i-mid
        if total < M:
            end=mid-1
        else:
            result=mid
            start=mid+1
    return result
answer=binary_search(0,N_list[N-1], N_list)
print(answer)