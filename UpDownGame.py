
# 업다운 게임은 컴퓨터가 생각한 숫자를 맞추는 게임
# 플레이어는 숫자를 입력하고 컴퓨터가 생각한 숫자와 비교하여 업(up) 혹은 다운(down) 힌트를 받아가며 숫자를 맞추는 게임

# 필수로 포함해야 할 기능
# 1. 1부터 100 사이의 랜덤한 숫자 생성
# 2. 플레이어는 숫자를 입력, 입력한 숫자와 비교하여 업 또는 다운 힌트 제공
# 3. 플레이어가 컴퓨터의 숫자를 정확히 맞히면 시도한 횟수를 알려줌
# 4. 플레이어가 숫자를 맞힐 때까지 위 과정을 반복


import random  # 랜덤 숫자 생성을 위한 라이브러리 호출

# 업다운 게임 함수


def game():
    computer = random.randint(1, 10)  # 랜덤 숫자
    player = int(input("숫자를 입력하세요 : "))  # 플레이어 숫자 입력

    cnt = 0  # 시도 횟수 초기화

    while True:

        # 플레이어가 1~100사이의 숫자를 입력하는지 확인
        if player in range(1, 101):
            cnt += 1  # 시도 횟수 추가

            # 입력한 숫자와 비교하기
            if player > computer:
                print("다운")
            elif player < computer:
                print("업")
            else:  # 랜덤 숫자와 일치하면 반복문 탈출
                print("맞았습니다")
                print(f"시도한 횟수 : {cnt}")
                break
        else:
            print("1부터 100 사이의 수를 입력하세요")

        player = int(input("숫자를 입력하세요 : "))
    return cnt


count = []  # 시도 횟수를 저장할 리스트

# 게임 실행
g = game()
count.append(g)  # 시도 횟수를 리스트에 추가

# 게임 반복 여부
while True:
    retry = input("다시 하시겠습니까? (y/n) : ")
    if retry != 'y':  # 대답이 y가 아니면 게임 종료
        print("게임을 종료합니다")
        break
    else:
        print(f"이전 게임 플레이어 최고 시도 횟수 : {min(count)}")
        g = game()
        count.append(g)
        continue
