'''
3
극장에서 n일 동안 매일 방문객 수를 조사함
가장 많은 방문객 수와 두번째로 많은 방문객 수의 차이
방문객의 수가 같은 날은 없다고 가정
1. 입력으로 주어진 리스트에서 가장 많은 방문객 수를 찾습니다.
2. 1번 단계에서 찾은 값을 제외하고, 나머지 값들로 이루어진 새로운 리스트를 만듭니다.
3. 2번 단계에서 만든 새로운 리스트에서 가장 큰 방문객의 수를 찾습니다.
4. 1번 단계와 3번 단계에서 구한 값의 차이를 구합니다.
'''
def func_a(arr, num): # num(최대) 값을 제거한 리스트를 반환하는 함수
    ret = []
    for i in arr:
        if i != num: # arr 리스트에서 num을 제외하고 복사
            ret.append(i)
    return ret

def func_b(a, b): # 두 값의 차이를 반환하는 함수
    if a> b:
        return a-b
    else:
        return b-a
    
def func_c(arr):  # arr 리스트 중 최대값 반환 함수
    ret = -1
    for i in arr:
        if ret < i:
            ret = i
    return ret

def solution(visitor):
    
    max_first = func_c(visitor)   # 1. 가장 많은 방문객 수
    visitor_removed = func_a(visitor, max_first) # 1이 제거된 리스트
    max_second = func_c(visitor_removed)  # 2번째로 가장 많은 방문객 수
    answer = func_b(max_first, max_second)  # 구한 값 차이
    return answer

