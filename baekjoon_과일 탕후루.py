from collections import defaultdict

def max_fruit_tanghuru(N, S):
    left = 0
    max_len = 0
    fruit_count = defaultdict(int)
    
    for right in range(N):
        # 현재 과일을 카운트에 추가
        fruit_count[S[right]] += 1
        
        # 과일 종류가 두 개 초과되면, left 포인터를 오른쪽으로 이동
        while len(fruit_count) > 2:
            fruit_count[S[left]] -= 1
            if fruit_count[S[left]] == 0:
                del fruit_count[S[left]]
            left += 1
        
        # 현재 구간의 길이 계산
        max_len = max(max_len, right - left + 1)
    
    return max_len

# 입력 처리
N = int(input())
S = list(map(int, input().split()))

# 결과 출력
print(max_fruit_tanghuru(N, S))
    