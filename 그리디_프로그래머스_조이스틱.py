
def solution(name):
    answer = 0
    move = len(name) - 1
    arr = [i for i in range(14)] + [i for i in range(12,0,-1)]
    
    for i in name:
        number = ord(i) - 65
        answer+=arr[number]

    for j in range(len(name)):
        next_j = j + 1
        while next_j < len(name) and name[next_j] == 'A':
            next_j += 1
        move = min(move, j + 2*(len(name) - next_j), 2*j + (len(name) - next_j))

    answer+=move
    return answer
print(solution("JEAAAROEAAN"))

