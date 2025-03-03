# 2025-02-03
# baekjoon 2607번 비슷한 단어
import sys
from collections import Counter

N = int(input())
first_voca = list(input().strip())
count_1 = Counter(first_voca)
answer = 0

for _ in range(N-1):
    compare_voca = list(input().strip())
    count_2 = Counter(compare_voca)
    diff1 = sum((count_1 - count_2).values())
    diff2 = sum((count_2 - count_1).values())

    if len(compare_voca) == len(first_voca) and diff1 + diff2 == 2:
        answer += 1
    elif abs(len(compare_voca) - len(first_voca)) == 1 and (diff1 == 1 or diff2 == 1):
        answer += 1
    elif len(compare_voca) == len(first_voca) and diff1 == diff2:
        answer += 1

print(answer)
