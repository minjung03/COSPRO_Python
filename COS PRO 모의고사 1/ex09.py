'''
9
중복되는 문자 제거
"senteeeencccccceeeee"라는 문장이 주어진다면 "sentence"라는 결과물이 나오게 
소문자 알파벳 characters 변수
한줄만 변경
'''

def solution(characters):
    result = [characters[0]] # 맨 앞글자 저장
    for i in range(1, len(characters)):
        if characters[i-1] != characters[i]:
            result.append(characters[i]) # 맨 앞글자는 이미 가져왔으므로, 다음 방 글자부터 저장한다
    return ''.join(result)

print(solution('senteeeencccccceeeee'))