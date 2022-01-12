# 교재 219p

def func_a(s) :
    s.sort()  # 정렬하기  (s = sorted(s))
    return s[len(s)-1], s[0]  # 정렬된 리스트에서 맨 앞/뒤의 값 가져오기

def func_b(s) :
    ret = 0
    for i in s:
        ret += i
    return ret

def solution(scores) :
    sum = func_b(scores)  # 총합 구하는 func_b 함수 호출
    max, min = func_a(scores)  # 최대,최소값 구하는 func_a 함수 호출
    return sum - max - min

scores = [100,50,30,40,60]
print(solution(scores))


#-----------리턴에 대하여

def a() :
    return 10, 20  # 파이썬에서는 여러개의 리턴이 가능하다

result1, result2 = a()  # 리턴 받은 값 순서대로 변수에 저장
print(result1)  # 10
print(result2)  # 20