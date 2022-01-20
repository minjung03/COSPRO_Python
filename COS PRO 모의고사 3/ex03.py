def solution(table) :
    answer = 0
    
    #  학생과 선생님이 같은 반이었던 횟수 세기
    students = []

    for i in range(1, len(table)) :  # 학생 1~5
        cnt = 0
        for j in range(5) :
            if table[0][j] == table[i][j] : # 선생님 반과 학생반 비교
                cnt += 1
        students.append(cnt)  
  
    # 가장 많은 학생 알아내기
    for i in students :
        if answer < i :
            answer = i
            
    return answer

table = [
    [2,6,1,7,3], # 선생님
    [2,9,4,6,8], # 학생1
    [6,3,4,7,1], # 학생2
    [8,6,9,7,3], # 학생3
    [4,6,5,9,2], # 학생4
    [4,6,5,9,2]  # 학생5
]

print(solution(table))