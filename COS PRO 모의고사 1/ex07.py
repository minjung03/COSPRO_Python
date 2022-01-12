'''
7
파일형식, 파일명, 파일크기
파일 형식이 "jpeg"이고, 파이릌기가 1,000보다 작은 파일만 업로드 할 수 있다.
파일정보: "jpeg,all.jpg,500"    결과: 업로드 가능
파일정보: "mpeg,all.mp3,500"    결과: 업로드 불가능 - 파일형식 불가
'''
def solution(file_info):
    success = 0
    fail = 0
    for f in file_info:
        splited = f.split(",") # ","를 기준으로 나눈 값이 splited 리스트로 저장
        if splited[0]=="jpeg" and int(splited[2])<1000 :
            # [0]에 있는 파일형식이 "jpeg" 인지, [2]에 있는 파일 크기(int로 변환)가 1000보다 작은지 비교
            success += 1
        else:
            fail += 1
    return success, fail

file_info = ["jpeg,all.jpg,500", "mpeg,all.mp3,500"]
s, f = solution(file_info)
print(f'{s} {f}')
