'''
(패턴화 익히기! 자리수 떼기)
5 
369게임을 하기 위해 숫자를 주면 박수를 몇번치는지 알아내는 함수
전달되는 number는 2자리 이상의 정수
'''
def solution(number):
    count = 0
    for i in range(1, number+1): # 1부터 number까지의 수를 확인해야하니 시작은 1, 끝은 number+1
        current = i
        while current != 0:  # while문의 변수는 무조건 한 번 값이 바뀐다(탈출해야 하니)
            unit = current % 10   # 일의 자리를 떼어낸다
            if unit == 3 or unit == 6 or unit == 9:
                count += 1
            current //= 10  # 확인한 일의 자리를 제거한 뒤 정수(//)로 저장
    return count

print(solution(12))