# 백준 - 17393번 다이나믹 롤러
# 알고리즘 - 이분탐색
# A_de의 현재 위치보다 오른쪽에 있으면서 점도 지수가 A(i)보다 낮은 칸을 칠한다. 이때, B_de는 오름차순

N=int(input())
A_de = list(map(int,input().split()))
B_de = list(map(int,input().split()))
answer =[]
for i in range(N):
    start = i+1
    end = N-1
    while(start <= end):
        mid = (start + end)//2
        if B_de[mid] > A_de[i]:
            end = mid - 1
        else:
            start = mid + 1
    answer.append(start- i-1)

# 언패킹(*)연산자 = 리스트, 튜플을 개별 요소로 풀어서 인수로 전달(이때, 구분자는 공백을 기준으로 함)
print(*answer)