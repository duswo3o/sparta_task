import random  # 랜덤 숫자 생성을 위한 라이브러리 호출

# 업다운 게임 함수
def game():
    # 1-1. 컴퓨터는 1부터 100 사이의 랜덤한 숫자를 생성
    computer = random.randint(1, 100)  # 랜덤 숫자

    # 1-2. 플레이어는 숫자를 입력하고
    player = int(input("숫자를 입력하세요 : "))  # 플레이어 숫자 입력

    cnt = 0  # 시도 횟수 초기화

    # 1-4. 플레이어가 컴퓨터의 숫자를 맟힐 때 까지 반복
    while True:

        # 추가 도전 과제 1. 플레이어가 입력한 숫자 범위를 벗어날 경우
        if player in range(1, 101):
            cnt += 1  # 시도 횟수 추가

            # 1-2. 입력한 숫자와 컴퓨터의 숫자를 비교하여 "업" 또는 "다운" 힌트를 제공
            if player > computer:
                print("다운")
            elif player < computer:
                print("업")
            else:  # 랜덤 숫자와 일치하면 반복문 탈출
                print("맞았습니다")
                # 1-3. 플레이어가 컴퓨터의 숫자를 정확히 맞히면 시도한 횟수를 알려줌
                print(f"시도한 횟수 : {cnt}")
                break

        # 추가 도전 과제 1. 적절한 안내 메시지를 출려갛여 유효한 범위 내의 숫자를 입력하도록 유도
        else:
            print("1부터 100 사이의 수를 입력하세요")

        player = int(input("숫자를 입력하세요 : "))
    return cnt  # 시도한 횟수를 리턴


count = []  # 시도 횟수를 저장할 리스트

# 게임 반복 여부
while True:
    # 게임 실행
    g = game()
    
    # 추가 도전 과제 3. 게임이 종료될 때 플레이어의 최고 시도 횟수 기록
    count.append(g)  # 시도 횟수를 리스트에 추가

    # 추가 도전 과제 2. 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료
    retry = input("다시 하시겠습니까? (y/n) : ")
    if retry != 'y':  # 대답이 y가 아니면 게임 종료
        print("게임을 종료합니다")
        break
    else:
        # 추가 도전 과제 3. 다음 게임에서 최고 시도 횟수 표시
        print(f"이전 게임 플레이어 최고 시도 횟수 : {min(count)}")
        continue
