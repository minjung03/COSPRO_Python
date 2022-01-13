'''
5
카페 회원들에게 일련번호 부여
가장 많은 글을 작성한 회원의 글 개수는 가장 적게 작성한 회원의 글 개수가 몇 배인지 
1. 리스트에 들어있는 각 회원별 글 개수를 셉니다.
2. 가장 많이 작성한 회원의 글 개수를 구합니다.
3. 가장 적게 작성한 회원의 글 개수를 구합니다.
4. 가장 많이 작성개수가 가장 적게 작성한 개수보다 몇 배인지 구함
'''
def func_a(arr):  # arr 요소들 값의 개수를 센 리스트 반환
    counter=[0 for _ in range(1001)]
    for i in arr:
        counter[i] += 1
    return counter

def func_b(arr):  # arr 중 최대값 반환
    ret=0
    for i in arr:
        if ret<i:
            ret=i
    return ret

def func_c(arr):  # arr 중 최소값 반환
    ret = func_b(arr) # ret를 arr 중 최대값으로 설정
    for i in arr:
        if i != 0 and ret > i: # 빈칸 : 최소값을 구해야하니 ret보다 작고, 아예 안 적은 사람들(0인)도 있응테니 '0이 아닐 때'
            # 이 부분 조건 조심!
            ret = i
    return ret

def solution(arr):
    counter=func_a(arr)  # 회원번호 개수를 세어 저장한 리스트 counter
    max_cnt=func_b(counter) # 작성된 긁의 개수 중 최대값
    min_cnt=func_c(counter) # 작성된 글의 개수 중 최소값
    return max_cnt // min_cnt


