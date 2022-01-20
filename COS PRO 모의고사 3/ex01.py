def solution(a,b) :
    answer = 0
    
    diff = (a-b) if a > b else b - a
    # a가 크다면 a-b, 아니라면 b-a
    # 파이썬 문법으로 이렇게 가능
    
    # diff = abs(a-b)
    # 이런 식으로도 가능
    
    answer = 10 / diff
    return answer * 60

print(solution(10,1)) # 66.6.. 1시간에 9km 차이(10-1)  10/9 = 1.1111, 1.1111*60 = 66.6666..
print(solution(10,5)) # 120    1시간에 5km 차이(10-5)  2시간에 10km 차이, 즉 2시간이 걸림
print(solution(10,8)) # 300
print(solution(8,10)) # 300
# 거리 = 속도 x 시간