import random

rsp = ['가위', '바위', '보']
player = input("가위, 바위, 보 중 하나를 선택하세요 : ")
computer = rsp[random.randint(0,2)]
record = {'승':0, "패": 0, "무승부":0}

