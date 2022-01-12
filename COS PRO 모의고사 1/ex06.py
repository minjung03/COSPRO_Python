'''
6
교차점의 개수를 구하는 함수
'''

def solution(left_rings): # left_rings = [0,3,1,4,2]
    answer = 0
    for i in range(len(left_rings)):     # i -> 왼쪽 고리 번호, left_rings[i] -> 오른쪽 고리 번호
        if left_rings[i] <= i:           # i가 1이라면 left_rings[i]는 0,1  즉, '왼쪽 / 오른쪽' 혹은 수평
            for k in range(i):           # 교차 조건을 판별 ('왼쪽 / 오른쪽'은 위에서 만족)
                if left_rings[k] > left_rings[i]: # 이전 인덱스에서 나의 오른쪽 고리 값보다 큰 것이 나왔을 때 ('왼쪽 \ 오른쪽')
                    answer += 1
    return answer

# 교차 조건 : 왼쪽 / 오른쪽 and 왼쪽 \ 오른쪽

print(solution([0,3,1,4,2]))  # 3
print(solution([0,1,2,3,4]))  # 0
print(solution([2,4,0,3,1]))  # 6
print(solution([3,1,2,4,0]))  # 6