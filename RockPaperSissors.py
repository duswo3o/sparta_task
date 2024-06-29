import random

# 가위바위보
rsp = ['가위', '바위', '보']

# 가위바위보 함수


def rock_paper_sissor(player, computer):
    print(f"사용자: {player}, 컴퓨터: {computer}")
    if player == computer:
        print("무승부!")
        return "무승부"
    elif (player == '가위' and computer == '보') | (player == '바위' and computer == '가위') | (player == '보' and computer == '바위'):
        print("사용자 승리!")
        return "승"
    else:
        print('사용자 패배!')
        return "패"


record = {'승': 0, "패": 0, "무승부": 0}  # 플레이어 통계
while True:

    player = input("가위, 바위, 보 중 하나를 선택하세요 : ")  # 플레이어의 선택
    computer = rsp[random.randint(0, 2)]  # 컴퓨터의 선택

    if player in rsp:
        game = rock_paper_sissor(player, computer)
        record[game] += 1
        retry = input("다시 하시겠습니까? (y/n) : ")
        if (retry == "y" or retry == "Y"):
            continue
        else:
            print("게암을 종료합니다.")
            break

    else:
        print("유효한 입력이 아닙니다")
        continue

print(f"승 : {record['승']} 패 : {record['패']} 무승부 : {record['무승부']}")
