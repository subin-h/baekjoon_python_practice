import sys
N,M = map(int,input().split())
keyword_list = []
usage_keyword = []

for i in range (N):
    keyword_list += sys.stdin.readline().split()
set_keyword = set(keyword_list)

for j in range (M):
    usage_keyword = sys.stdin.readline().strip().split(',')
    set_usage = set(usage_keyword)
    set_keyword -= set_usage
    print(len(set_keyword))