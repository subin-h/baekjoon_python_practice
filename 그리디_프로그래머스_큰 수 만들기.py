def solution(number, k):
    answer = ''
    stack =[]
    removed_count = 0
    for i in number:
        while stack and removed_count < k and stack[-1] < i:
            stack.pop()
            removed_count +=1
        stack.append(i)

    return ''.join(stack[:len(stack)-(k-removed_count)])