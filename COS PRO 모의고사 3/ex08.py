from typing import AnyStr


def solution(password, key) :
    answer = 0
    match_cnt = 0
    
    for k in key :
        for p in password :
            if k == p :  # key에 있는 값이 password에 들어있다면
                match_cnt += 1
                break
            
    if match_cnt >= len(key) : # match_cnt는 'key보다' 크거나 같아야 한다
        answer = 1
        
    return answer

print(solution('GGGa9##', 'Ga9#')) # 1
print(solution('GGGa##', 'Ga9#'))  # 0