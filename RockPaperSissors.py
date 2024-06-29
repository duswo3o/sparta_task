import random

# 가위바위보
rsp = ['가위', '바위', '보']

player = input("가위, 바위, 보 중 하나를 선택하세요 : ") # 플레이어의 선택
computer = rsp[random.randint(0,2)] # 컴퓨터의 선택

record = {'승':0, "패": 0, "무승부":0} # 플레이어 통계

print(f"사용자: {player}, 컴퓨터: {computer}")
if player == computer :
    record["무승부"] += 1
    print("무승부!")
elif (player == '가위' and computer == '보') | (player == '바위' and computer == '가위') | (player == '보' and computer == '바위') :
    record["승"] += 1
    print("사용자 승리!")
else :
    record["패"] += 1
    print('사용자 패배!')

print(f"승 : {record['승']} 패 : {record['패']} 무승부 : {record['무승부']}")