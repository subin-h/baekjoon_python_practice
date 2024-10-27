import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, k, t, m = map(int, input().split())

    scores = [[0] * (k + 1) for _ in range(N + 1)]
    submission_count = [0] * (N + 1)
    last_submission_time = [0] * (N + 1)

    for log_index in range(m):
        i, j, s = map(int, input().split())
        if s > scores[i][j]:
            scores[i][j] = s
        submission_count[i] += 1
        last_submission_time[i] = log_index + 1
    
    results = []
    for n in range(1, N + 1):
        total_score = sum(scores[n])
        total_submissions = submission_count[n]
        last_time = last_submission_time[n]
        results.append((total_score, total_submissions, last_time, n))

    results.sort(key=lambda x: (-x[0], x[1], x[2]))

    rank = 1
    for result in results:
        if result[3] == t:
            print(rank)
            break
        rank += 1

