from collections import deque
def solution(priorities, location):
    priorities[location] = float(priorities[location])
    queue = deque(priorities)
    print_priroities = []

    while queue:
        x = queue.popleft()
        for i in queue:
            if x < i:
                queue.append(x)
                break
            print_priroities.append(x)
    return print_priroities

answer = solution([2, 1, 3, 2], 2)
