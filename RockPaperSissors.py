import random

# 가위바위보
rsp = {'가위':0, '바위':1, '보':2}

player = input("가위, 바위, 보 중 하나를 선택하세요 : ") # 플레이어의 선택
computer = list(rsp.keys())[random.randint(0,2)] # 컴퓨터의 선택

record = {'승':0, "패": 0, "무승부":0} # 플레이어 통계

print(computer,"\n",player)