def solution(string) :
    answer = 0
    number = 0
    s = string+''
    
    for c in s :
        if '0' <= c and c <= '9':  # 숫자라면  ('0' <= c <= '9') *꼭 알아두기
            number = number * 10 + int(c) 
        else :
            answer += number  # 합계
            number = 0
    return answer

print(solution("Korean world cup 2018. olympic stadium 10. 11 pm 1."))