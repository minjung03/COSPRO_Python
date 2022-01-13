'''
8
이름에 특정 문자가 포함된 개수 구하기
대조영빌딩
4F  Kickboard Association
3F  Common Engineering
2F  Adios
1F  CafeMasita. Ltd
회사 이름에 'A' 또는 'K'가 들어가는 회수 세기
'''
def solution(name_list):
    answer = 0
    for name in name_list:
        for char in name:
            if char.find('A') > -1 or char.find('K') > -1 :  # if문은 true/false 값으로 판단해야한다
                # find() : 해당 값이 있는지 없는지 체크 (있다면 index, 없다면 -1을 리턴)
                answer += 1
                break
    return answer

print(solution(['Kickboard Association', 'Common Engineering', 'Adios', 'CafeMasita. Ltd']))
