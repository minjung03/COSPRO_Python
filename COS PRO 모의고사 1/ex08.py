'''
8
거꾸로 읽어도 같은 것: 회문
"racecar"과 "noon"은 회문
소문자 알파벳, 공백(' '), 마침표('.')로 이루어진 문장
회문인지 점검
문장 내에서 알파벳만 추출하였을 때만을 고려 즉
"never odd or even."은 회문
'''

def solution(sentence):
    filtered = []
    for s in sentence:
        if s != ' ' and s != '.':
            filtered.append(s)
    before = ''.join(filtered)  # before에 공백과 .이 제거된 문자열을 넣는다
    filtered.reverse()
    after = ''.join(filtered)  
    return before == after

print(solution('never odd or even'))
