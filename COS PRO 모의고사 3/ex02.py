def func_a(arr):
    total = 0
    for i in arr :
        total += i
    return total

def solution(total, arr):
    result = []
    req_total = func_a(arr) # 신청한 예산액 총합 구하기
    for i in arr :
        if req_total >  total : # 예산 총액과 비교
            result.append(total // len(arr)) # 신청긍이 더 크다면 예산 총액 나누기
        else :
            result.append(i) # 신청긍이 더 작다면 그대로 배분
            
    return result
    
    
print(solution(500, [120,90,140,150]))  # [120, 90, 140, 150]
print(solution(500, [200,110,140,150])) # [125, 125, 125, 125]