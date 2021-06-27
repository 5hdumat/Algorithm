# O(N log N)
unsorted_list = [int(x) for x in input().split()]

def merge(left, right):
    i = 0
    j = 0
    sorted_list = []
    
    # 둘중 하나가 만족할때까지 append
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
       
    # 남은 값들을 넣어준다     
    while i < len(left):
        sorted_list.append(left[i])
        i += 1 
    
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    
    return sorted_list
        
# n / 2로 나눠 1개의 요소가 남기까지 재궈호출 합니다.
# 그 다음 2개씩의 요소들을 반복적으로 병합합니다.
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]
    
    left1 = merge_sort(left) ## 재귀를 이용하여 왼쪽 리스트를 다시 나눕니다.
    right1 = merge_sort(right) ## 오른쪽도 마찬가지로 다시 나눕니다.
    
    print(left1, right1)

merge_sort(unsorted_list)