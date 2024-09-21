import sys
input = sys.stdin.readline
N= int(input())
arr=[]
arr=[(int(data[0]), data[1]) for data in (input().split() for _ in range(N))]
# split - 공백으로 구분하여 리스트로 저장
arr.sort(key=lambda x:x[0])
print('\n'.join(' '.join(map(str, _arr)) for _arr in arr))
