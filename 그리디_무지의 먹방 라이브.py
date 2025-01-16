def solution(number, k):
    answer = ''
    stack = []  # 스택을 사용하여 숫자들을 저장
    removed_count = 0  # 제거한 숫자 수

    for digit in number:
        # 현재 스택에 마지막 숫자보다 더 큰 값이 오면 스택에서 제거
        while stack and removed_count < k and stack[-1] < digit:
            stack.pop()  # 더 작은 숫자는 제거
            removed_count += 1
        print(stack, removed_count)
        stack.append(digit)  # 현재 숫자는 스택에 추가
    
    # 만약 k번을 제거하지 못했다면 남은 숫자들을 잘라내어 출력
    return ''.join(stack[:len(stack) - (k - removed_count)])

print(solution("10", 1))