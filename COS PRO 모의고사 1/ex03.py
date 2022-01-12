
def solution(scores):
    count = 0
    for s in range(len(scores)):  # range()는 정수값을 작성해야하니 scores의 길이를 len()으로 가져온다
        if scores[s] <= 200:
            count += 1
    return count

scores = [210,200,300,180,50]
print(solution(scores))

