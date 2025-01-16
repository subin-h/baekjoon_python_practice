def solution(n, lost, reserve):
    students = [1] * (n+2)
    lost.sort()
    reserve.sort()
    for i in lost:
        students[i] -= 1

    for j in reserve:
        students[j] += 1
    
    print(students)
    for k in reserve:
        if students[k-1] == 0 and students[k] == 2:
            students[k-1] += 1
            students[k] = 1

        elif students[k+1] == 0 and students[k] == 2:
            students[k+1] = 1
            students[k] = 1
    
    print(students)
    answer = students.count(1) + students.count(2) - 2
    return answer

'''lost_list = list(set(lost) - set(reserve))
reserve_list = list(set(reserve) - set(lost))

for r in sorted(reserve_list):
    if r-1 in lost_list:
        lost_list.remove(r-1)
    elif r+1 in lost_list:
        lost_list.remove(r+1)

return n - len(lost_list)'''