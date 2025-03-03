# 2025-02-01
# baekjoon 28353번 고양이 카페

# N = 고양이 수, K = 고양이 무게 합 limit, cats = 고양이 무게 리스트
# 인당 고양이 두마리씩, 최대 몇 명까지 가능한가

# 그리디 알고리즘 (투 포인터)

import sys

N,K = map(int,input().split())
cats = sorted(list(map(int,sys.stdin.readline().split())))

count = 0
start = 0
end = len(cats) - 1

while(end>start):
    if cats[end] + cats[start] > K:
        end -= 1
    else:
        count +=1
        end -= 1
        start += 1

print(count)