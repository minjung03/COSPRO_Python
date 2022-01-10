
# 파이썬 문제 풀이
scores = [10,3,20,50]

#1 
def sum_list(scores) :
    pass  # 빈칸(아무 것도 안한다는 것)
    result = 0
    
    for i in scores :
        result += i  # 들여쓰기로 함수 영역 표시
        
    return result

#2 
def max_list(scores) :
    max_num = scores[0]
    
    for i in scores :
        if max_num < i :
            max_num = i 
      
    """ 이런 방법도 있다 (C, JAVA와 비슷) 
    for i in range(1, len(scores)) :
        if max_num < scores[i] :
            max_num = scores[i]
    """     
    return max_num

#3 
def min_list(scores) :
    min_num = scores[0]
    
    for i in scores :
        if min_num > i :
            min_num = i      
        
    return min_num

#4
def avg_list(scores) :
    sum_num = 0
    
    for i in scores :
        sum_num += i  
    
    return sum_num/len(scores)

# 4-2 (len() 함수 사용하지 않고)
def avg_list2(scores) :
    sum_num = 0
    list_cnt = 0
    
    for i in scores :
        sum_num += i  
        list_cnt += 1
    
    return sum_num / list_cnt

#5
def count_even(scores) :
    count = 0
    
    for i in scores :
        if not(i%2) :  # i%2==0 이라면
            count += 1
            
    return count
     
#6 
def make_list(list_num) :
    lists = [0 for i in range(list_num)]  # 리스트 길이를 list_num으로 지정하고 0으로 초기화
    print([0 for _ in range(list_num)])  # i를 실제로 사용하지는 않으니 _ 으로 바꾸기도 가능
    return lists      # range(6) -> 0,1,2,3,4,5

#7
def count_even2(scores) :
    count = 0
    
    for i in scores :
        if not(i%2) and i>10 :  # i%2==0 이면서 i가 10보다 클 때
            count += 1
            
    return count    
    
    
# 1 (숫자가 들어있는 리스트의 합계)
print(sum_list(scores)) # 83
print(sum(scores)) # sum() 이란 기본 함수가 존재한다. 
# 동일한 이름이 있으면 함수 기능을 잃게되니 변수명을 sum, max,min 등으로 주지 말라는 것**
# 물론 지금 코드에서는 선언 영역이 있으니 위 함수 안에서 sum을 선언해도 작동은 하지만 항시 유의하기

# 2 (최대값 구하기)
print(max_list(scores)) # 50
print(max(scores)) 

# 3 (최소값 구하기)
print(min_list(scores)) # 3
print(min(scores))

#4 (평균 구하기)
print(avg_list(scores)) # 20.75
print(avg_list2(scores))
print(sum(scores)/len(scores))

#5 (짝수의 갯수 구하기)
print(count_even(scores)) # 3
print(len([item for item in scores if item % 2 == 0])) # 리스트 한 줄로 생성하기
# print(len([변수 for 꺼낸변수 in 덩어리 if 조건]))
 
#6 (N개의 0을 가진 리스트 생성하기)
print(make_list(6)) # [0, 0, 0, 0, 0, 0]

#7 (짝수이면서 10보다 큰 수 객수 세기)
print(count_even2(scores))


