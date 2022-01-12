'''
10
1 이상의 정수가 들어있는 리스트의 평균을 구하고, 평균 미만인 값은 몇개 인지 구하라
예: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]이라면 평균은 5, 평균 미만인 값은 4개
한줄만 변경
'''
def solution(data):
    total = 0
    for i in data:
        total += i
    cnt = 0
    average = total // len(data)
    for i in data:
        if i < average:  # 평균 미만을 구해야하니 =는 빼기
            cnt+=1
    return cnt

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(solution(data))