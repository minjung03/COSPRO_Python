"""
한 학생의 과목별 점수가 들어있는 배열이 주어졌을 때, 
이 학생의 최고 점수와 최저 점수를 제외한 나머지 점수들의 합계를 구하려 합니다. 
이를 위해 다음과 같이 4단계로 프로그램 구조를 작성했습니다.

1. 모든 과목 점수의 합을 구합니다.
2. 최고 점수를 구합니다.
3. 최저 점수를 구합니다.
4. (모든 과목 점수의 합) - (최고 점수) - (최저 점수)의 값을 return 합니다.

학생의 과목별 점수가 들어있는 배열 scores가 매개변수로 주어질 때, 
학생의 과목별 점수에서 최고 점수와 최저 점수를 제외한 나머지 점수의 합을 return 하도록 solution 함수를 작성하려 합니다. 
위 구조를 참고하여 코드가 올바르게 동작할 수 있도록 빈칸에 주어진 funca, funcb, func_c 함수를 알맞게 채워주세요.

"""

def func_a(s):
    ret = 0
    for i in s:
        if i > ret:
            ret = i
    return ret

def func_b(s):
    ret = 0
    for i in s:
        ret += i
    return ret

def func_c(s):
    ret = 101
    for i in s:
        if i < ret:
            ret = i
    return ret


def solution(scores):
    sum = func_b(scores)
    max_score = func_c(scores)
    min_score = func_a(scores)
    return sum - max_score - min_score