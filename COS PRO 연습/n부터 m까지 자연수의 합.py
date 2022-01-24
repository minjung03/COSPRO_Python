"""
두 자연수 n부터 m까지의 합을 구하려고 합니다.
이를 위해 다음과 같이 3단계로 간단히 프로그램 구조를 작성했습니다.

1. 1부터 m까지의 합을 구합니다.
2. 1부터 n-1까지의 합을 구합니다.
3. 1번 단계에서 구한 값에서 2번 단계에서 구한 값을 뺍니다.

두 자연수 n과 m이 매개변수로 주어질 때, n 부터 m 까지의 합을 return 하도록 solution 함수를 작성했습니다. 
이때, 위 구조를 참고하여 중복되는 부분은 func_a라는 함수로 작성했습니다. 
코드가 올바르게 동작할 수 있도록 빈칸을 알맞게 채워주세요.

"""

def func_a(k):
    sum = 0
    for i in range(k):  # range(숫자) : 0부터 숫자-1 까지 반복
        sum += i+1      # 1부터 더해야하니 +1한 값을 더한다
    return sum

def solution(n, m):
    sum_to_m = func_a(m)
    sum_to_n = func_a(n-1)
    answer = sum_to_m - sum_to_n
    return answer