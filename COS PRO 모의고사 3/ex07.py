def solution(a,b) :
    result = [0,0]
    for i in range(3):
        temp = b
        for k in range(3) :
            if a%10 == temp%10 :  # a%10 : 3  temp%10 : 5 -> 4 -> 3
                if i==k :
                    result[0] += 1
                else :
                    result[1] +=1
            temp //= 10  # temp를 10으로 나누어 넣음 (34 -> 3)
        a //= 10  # a도 바뀌어야 함
    return result

print(solution(123,345))  # [0, 1]