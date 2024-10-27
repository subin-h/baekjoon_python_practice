X,Y=map(int,input().split())
Z=int(100*Y/X)
def binary_search(start, end, number, victory):
    if X==Y or Z==99.0:
        return -1
    while(start<=end):
        mid=(start+end)//2
        result_X=number+mid
        result_Y=victory+mid
        ch_Z=int(100*result_Y/result_X)
        if ch_Z > Z:
            result=mid
            end=mid-1
        else:
            start=mid+1
    return result
play=binary_search(0, X, X, Y)
print(play)


