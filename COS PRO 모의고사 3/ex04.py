def solution(walls) :
    answer = 0
    painted_walls = 0
    hour = 1
    
    while painted_walls < walls :
        painted_walls = (hour) + (hour//2) + (hour//4) # 1 시간당 칠해지는 벽
        # a는 1시간에 하나의 벽, b는 2시간에 하나의 벽, c는 4시간에 하나의 벽
        hour += 1
        
    answer = hour-1 # hour이 1로 초기화 되어있으니 결과에 -1 해주기
    
    return answer


print(solution(7))   # 4