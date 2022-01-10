# --------------------------------문법 정리

# 한 줄 주석
""" 여러줄 주석으로 보면 됨 (''' 도 가능) """ 

# ()는 산술 시 우선 순위 지정 때나 함수 매개 변수에만 작성한다

# print(출력)
name = "minjung"
age = 20
print(f'name : {name}, age : {age}') # 이러한 출력문 사용할 것임 (다양하다)


# 연산자
a = 10 # 파이썬에는 ++,-- 연산자가 없다
a += 1 # 이런식으로 사용

print(10**2)      # 10의 2제곱 (** : 거듭제곱)
print(10/3)       # 10을 3으로 나눈 값의 '실수'
print(10//3)      # 10을 3으로 나눈 값의 '정수'


# 조건문
# if ~ elif ~ else 로 사용

# 반복문
# for ~ in ~ : 로 사용
list2 = [1,2,3,4,5]
for item in list2 :   # cos pro 에서는 이런 식으로 작성되있을 것
    print(item)
    
for i in range(0,4,1) :  # range() 는 C에서 for문 중 index를 세팅하는 것이라 생각하기
                         # 0에서 4까지 1씩 증가 (4는 안감* / 처음(0)이나 1씩 증가 요런 것은 생략해도 가능)
    print(list2[i])

for i in range(len(list2)) :
    print(list2[i])
    
for index, value in enumerate(list2) : # index와 value를 같이 가져오고 싶을 때
    print(f'{index + 1}번, {value}')

# 인덱싱
print('hello'[1])   # 'e' 출력
print('hello'[-1])  # 'o' 출력
print('hello'[-2])  # 'l' 출력
print('hello'[1:3])  # 'el' 출력 ("뒤에 것은 포함 X" / 1~2 출력)
print('hello'[:3])  # 'hel' 출력 (앞 생략 가능 / 처음부터 2 까지 출력)
print('hello'[1:])  # 'ello' 출력 (뒤 생략 가능 / 처음의 1 제외 출력)
print('hello'[:])  # 'hello' 출력 (전체 출력)

print('hello'.count('l')) # 2 (카운트 문제 많이 나온다)
print('hello'.find('o'))  # 4 (찾는 값이 없으면 -1 반환)
print('hello'.index('l')) # 2
# print('hello'.index('z')) # 이건 에러

list3 = [1,2,3]
print(list3[2])  # 3


# 문자열
print('hello' + 'world') # 문자열 붙이기

a = 'hello world good lunch'
b = a.split(' ')       # 문자열 자르고 리스트로 반환 (' ' 를 기준으로)
print(b)     
c = '-'.join(b);       # 리스트를 문자열로 바꾸기 (리스트 값 사이 '-' 를 붙여서)
print(c)

print('-' * 30)  # 문자열 잇기 (-가 30개 출력 / '-'+'-'+'-'.....)


# 리스트 (C의 배열 느낌 / 조금 더 유연하다)

#| len(리스트명) | 길이 |
#| 리스트명.append(obejct) | 추가 |
#| 리스트명 += 리스트명2 | 추가 |
#| 리스트명.copy() | 복사 |
#| 리스트명.count(value) | 세기 |
#| 리스트명.index(value) | 찾기 ⇒ index or ValueError |
#| 리스트명.insert(index, value) | 추가 |
#| 리스트명.remove(value) | 삭제 |
#| 리스트명.sort() | 정렬 |
#| 리스트명.reverse() | 뒤집기 |

smtm = ['원슈', '자이언티', '소코도모']
smtm.append('조광일')
print(smtm)

smtm2 = smtm.copy()
smtm2.append([1,2])
print(smtm2)

smtm2 = smtm2 + [1,2]
print(smtm2)

print(smtm2.count(2))
print(smtm2.index(2))
smtm2.remove(2)
print(smtm2)

 # 리스트 사용 불가 메서드 (.sort() .reverse())
smtm.sort()  # 값이 정렬된다
print(smtm)
smtm.reverse()
print(smtm)  # 값이 반전된다 (정렬은 X)

 # 리스트 사용 가능
ex = sorted(smtm)  # 원래의 값은 변하지 않아 어딘가에 넣어줘야 한다
print(ex)

print(len(smtm)) # 리스트 길이


# 변환 함수
# str <-> int
int("123") # 자료형을 함수처럼 호출하면 변환 끝
str(123)
d = list("123") # 리스트도 함수처럼 호출해 리스트화 가능 (String을 한글자씩 꺼내어 사용)
print(d)