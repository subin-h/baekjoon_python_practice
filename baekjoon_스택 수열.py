N = int(input())
number = [int(input()) for _ in range(N)]
stack =[]
result = []
current_num = 1

for i in number:
    while current_num <= i:
        stack.append(current_num)
        result.append('+')
        current_num += 1
    
    if stack and stack[-1] == i:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        break
else:
    print("\n".join(result))
