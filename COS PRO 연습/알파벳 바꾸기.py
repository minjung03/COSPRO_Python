"""

문자열이 주어졌을 때, 문자열에서 'a'는 'z'로, 'z'는 'a'로 바꾸려고 합니다. 
예를 들어 주어진 문자열이 "abz"라면 "zba"라는 문자열을 만들면 됩니다.

문자열 s가 매개변수로 주어졌을 때, 문자열에서 'a'는 'z'로, 'z'는 'a'로 바꾸어 return 하도록 solution 함수를 작성했습니다. 
그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다. 
주어진 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

"""

def solution(s):
    s_lst = list(s)
    n = len(s)
    for i in range(n):
        if s_lst[i] == 'a':
            s_lst[i] = 'z'
        elif s_lst[i] == 'z':  # else if는 elif로 줄여쓴다
            s_lst[i] =  'a'
    return "".join(s_lst)


# 이 외
s = 'abz'
print(s[0])  # a
s[0] = 'z'   # 오류 - str이 상수라는 것
