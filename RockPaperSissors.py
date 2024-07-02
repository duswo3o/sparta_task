import random

# 가위바위보 함수
def rock_paper_sissor(player, computer):
    print(f"사용자: {player}, 컴퓨터: {computer}")
    # 2-3. 플레이어와 컴퓨터의 선택을 비교하여 승패를 판정
    # 2-4. 결과를 출력하여 플레이어가 이겼는지, 컴퓨터가 이겼는지, 비겼는지 알려줌
    if player == computer:
        print("무승부!")
        return "무승부"
    elif (player == '가위' and computer == '보') | (player == '바위' and computer == '가위') | (player == '보' and computer == '바위'):
        print("사용자 승리!")
        return "승"
    else:
        print('사용자 패배!')
        return "패"

# 가위바위보
rsp = ['가위', '바위', '보']
record = {'승': 0, "패": 0, "무승부": 0}  # 플레이어 통계

while True:
    # 2-1. 플레이어가 가위, 바위, 보 중 하나를 입력
    player = input("가위, 바위, 보 중 하나를 선택하세요 : ")

    if player in rsp: # 입력이 가위, 바위, 보 중에 있다면

        # 2-2. 컴퓨터도 무작위로 가위, 바위, 보 중 하나를 선택
        computer = rsp[random.randint(0, 2)]
        game = rock_paper_sissor(player, computer) # 가위바위보 게임 실행

        # 추가 도전 과제 1. 게임의 승, 무, 패 횟수를 기록
        record[game] += 1 # 가위바위보 결과(승/패/무승부)를 플레이어 통계에 업데이트

        # 추가 도전 과제 3. 게임 재시작 여부 묻기
        retry = input("다시 하시겠습니까? (y/n) : ")

        # 추가 도전 과제 2. 플레이어가 입력할 때 대소문자를 구분하지 않도록 프로그램 개선
        # 추가 도전 과제 3. 게임 재시작 여부에 따라 게임을 초기화하거나 종료
        if (retry == "y" or retry == "Y"): # 대답이 y 또는 Y인 경우 게임 다시 하기
            continue
        else: # 그 외의 대답은 게임 종료
            print("게암을 종료합니다.")
            break

    else:
        print("유효한 입력이 아닙니다")
        continue

# 추가 도전 과제 1. 게임 종료 시에 플레이어에게 통계를 제공
print(f"승 : {record['승']} 패 : {record['패']} 무승부 : {record['무승부']}")
