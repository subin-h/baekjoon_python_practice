N=int(input())
current_number = list(map(int,input().strip()))
target_number = list(map(int,input().strip()))

test2 = current_number.copy()
test2[0] = 1 - test2[0]
test2[1] = 1 - test2[1]

def solve(arr):
    answer = 0
    for i in range(1,N):
        if i == (N-1):
            if arr[i-1] != target_number[i-1]:
                answer +=1
                arr[i-1] = 1 - arr[i-1]
                arr[i] = 1 - arr[i]
            continue
        if arr[i-1] != target_number[i-1]:
            answer +=1
            arr[i-1] = 1 - arr[i-1]
            arr[i] = 1 - arr[i]
            arr[i+1] = 1 - arr[i+1]
    return answer,arr

answer = -1
answer1,current_number = solve(current_number)
answer2, test2 = solve(test2)

if test2 == current_number == target_number:
    answer = min(answer1, answer2+1)
elif test2 == target_number:
    answer = answer2+1
elif current_number == target_number:
    answer = answer1

print(answer)