# 2025-01-25
# baekjoon 1181번 단어 정렬

# 알파벳 소문자로 이루어진 N개의 단어를 2가지 조건으로 정렬하라. (단, 단어 중복 X)
# 1. 길이가 짧은 것부터 
# 2. 길이가 같다면 사전 순

import sys

N = int(input())
input = sys.stdin.readline

words = set([input() for _ in range(N)])
sorted_words = sorted(words,key = lambda x:(len(x),x))
print("".join(sorted_words))