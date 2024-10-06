T=int(input())
for _ in range(T):
    N=int(input())
    arr=list(map(int,input().split()))
    arr_rev=arr[::-1]
    max_sav=arr_rev[0]
    answer=0
    for i in range(1, len(arr_rev)):
        if max_sav>arr_rev[i]:
            answer+=max_sav-arr_rev[i]
        else:
            max_sav=arr_rev[i]
    print(answer)

