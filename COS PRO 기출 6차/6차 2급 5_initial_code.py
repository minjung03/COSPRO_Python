def solution(money, price, n):
    answer = 0
    empty_bottle = answer = money // price
    while n <= empty_bottle:  # while문을 빠져나가게 해야한다, n 혹은 empty_bottle 변화시키기
        empty_bottle = empty_bottle - n   # empty_bottle을 n개 만큼 소비해야 한다
        answer += 1
        empty_bottle += 1
    
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
money1 = 8
price1 = 2
n1 = 4
ret1 = solution(money1, price1, n1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

money2 = 6
price2 = 2
n2 = 2
ret2 = solution(money2, price2, n2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")