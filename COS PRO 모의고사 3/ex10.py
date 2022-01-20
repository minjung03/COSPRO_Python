def solution(strings) :
    result = 0
    
    for s in strings :
        length = len(s)  # 13
        result += (length // 4)  # 13//4
        
        if length % 4 != 0 :  # 나머지가 생겼을 때 1을 증가해야하니 != 로 작성
            result += 1
    return result


print(solution("abcdef1234567"))