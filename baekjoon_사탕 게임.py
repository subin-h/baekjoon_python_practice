N = int(input())
candy = [list(input().strip()) for _ in range(N)]
max_count = 0

for i in range(N):
    for j in range(0,N-1):
        if candy[i][j] != candy[i][j+1]:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            count1 = 1
            count = 1
            
            for row in range(N):
                for column in range(N-1):
                    if candy[column][row] == candy[column+1][row]:
                        count1 += 1
                        max_count = max(count1,max_count)
                    else:
                        count1 = 1
                count1 = 1

            for column in range(N):
                for row in range(N-1):
                    if candy[column][row] == candy[column][row + 1]:
                        count += 1
                        max_count = max(count,max_count)
                    else:
                        count = 1
                count = 1
            
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

for i in range(N):
    for j in range(0,N-1):
        if candy[j][i] != candy [j+1][i]:
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
            count_column = 1
            count1_column = 1

            for column in range(N):
                for row in range(N-1):
                    if candy[column][row] == candy[column][row + 1]:
                        count_column += 1
                        max_count = max(count_column,max_count)
                    else:
                        count_column = 1
                count_column = 1

            for row in range(N):
                for column in range(N-1):
                    if candy[column][row] == candy[column+1][row]:
                        count1_column += 1
                        max_count = max(count1_column,max_count)
                    else:
                        count1_column = 1
                count1_column = 1

            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]

print(max_count)