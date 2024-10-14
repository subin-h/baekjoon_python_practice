#예제) 퀵 정렬 소스코드
array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start +1
    right= end
    while left <= right:
        # end까지, pivot보다 값이 작은 경우
        while left <= end and array[left] <= array[pivot]:
            left +=1
        # start 까지, pivot보다 값이 큰 경우
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # left(큰 값), right(작은 값) 교환 (오름차순)
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    #분할 이후, 이전 pivot 전후로 재귀 호출(right==이전 pivot)
    quick_sort(array, start, right-1)
    quick_sort(array, right +1, end)

quick_sort(array,0,len(array)-1)
print(array)