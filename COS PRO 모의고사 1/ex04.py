def solution(price, grade):
    answer = 0
    
    # 각 등급에 따라 원금 + 관세를 더한 값 구하기
    if grade == 'S' :
        answer = price + (price * 0.05) 
    elif grade == 'G' :
        answer = price + (price * 0.1)
    elif grade == 'V' :
        answer = price + (price * 0.15)  
    return int(answer)

print(solution(1000,'S'))
