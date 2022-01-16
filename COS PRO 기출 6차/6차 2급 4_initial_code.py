#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(cards):
    #여기에 코드를 작성해주세요.
    answer = 0
    
    # 카드 색깔 별로 세기
    total= 0
    
    counter = [0,0,0]
    for card in cards :    # ['blue', '2'] -> ['red', '5'] -> ['black', '3']
        
        color = card[0]  # 'blue'
        number = card[1] # '2'
        
        if color == 'red' :
            counter[0] += 1   
        elif color == 'black' :
            counter[1] += 1
        else :
            counter[2] += 1
            
        # 합계 구하기   
        total += int(number)  # int 변환 시켜주기*

        
    for i in counter :
        if i == 3 :
            answer = total * 3
        elif i == 2 :
            answer = total * 2
        else :
            answer = total
            
    # **이렇게도 가능
    # weigter = max(counter) # 최대 값을 뽑아준다
    # answer = total * weigter 
            
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
ret1 = solution(cards1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

cards2 = [["blue", "2"], ["blue", "5"], ["black", "3"]]
ret2 = solution(cards2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")