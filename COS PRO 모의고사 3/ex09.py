def solution(scores) :
    result = [0,0,0,0]
    
    for i in range(4) :
        for k in range(4) :
            if i != k :
                result[i] += scores[i][k] * 2 # 이긴 팀 승점이 2점이니 *2 해주기
    return result


scores = [
    [-1,1,0,0],
    [0,-1,0,1],
    [1,1,-1,1],
    [1,0,0,-1]
]

print(solution(scores)) # [2,2,6,2]