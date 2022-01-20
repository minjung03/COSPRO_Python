def solution(mho_cards, mhe_cards) :
    result = -1
    
    # 각자가 이긴 횟수 세기
    counter = [0,0] # 민호, 민희 횟수 카운트
    
    for i in range(len(mho_cards)) :
        if mho_cards[i] > mhe_cards[i] :
            counter[0] += 1
        else :    
            counter[1] += 1
            
    if counter[0] > counter[1] :  # 민호 이김
        result = 1 
    elif counter[0] < counter[1] : # 민희 이김
        result = 0
    else :  # 무승부
        result = -1
    
    return result


# 테스트 코드
import random # 랜덤

# 1 ~ 13 까지의 수가 랜덤하게 들어있는 리스트
mho_cards = list(range(1, 13+1))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
random.shuffle(mho_cards) # 섞어짐

mhe_cards = list(range(1, 13+1))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
random.shuffle(mhe_cards) # 섞어짐

print(mho_cards, mhe_cards)
print(solution(mho_cards, mhe_cards))

    