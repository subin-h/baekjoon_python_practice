import sys
N=int(input())
N_list=sorted(map(int,sys.stdin.readline().split()))
M=int(input())
M_list=list(map(int,sys.stdin.readline().split()))

def binary_search(target, list, start, end):
    if start > end:
        return 'no'
    mid = (start+end) // 2
    if list[mid] == target:
        return 'yes'
    elif list[mid] > target :
        return binary_search(target, list, start, mid-1)
    else:
        return binary_search(target, list, mid+1, end)
    
result=[]
for i in M_list:
    result.append(binary_search(i, N_list, 0, N-1))
print(' '.join(result))
        