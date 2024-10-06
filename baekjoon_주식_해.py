import sys
input = sys.stdin.readline

def solution():
    n=int(input())
    array=list(map(int, input().split()))
    idx=0
    answer=0
    while True:
        maximum = max(array)
        idx = len(array) - 1 - array[::-1].index(maximum)
        if idx> 0:
            answer += (maximum * idx) - sum(array[:idx])
        
        if idx == n-1:
            return answer
        
        idx +=1
        array = array[idx:]
        if len(array) <= 1:
            return answer
t = int(input())
for i in range(t):
    print(solution())