import random

vp = [{'name': 'team1', 'pts': 0}, {'name': 'team2', 'pts': 0}, {'name': 'team3', 'pts': 0},
      {'name': 'team4', 'pts': 0}, {'name': 'team5', 'pts': 0}, {'name': 'team6', 'pts': 0},
      {'name': 'team7', 'pts': 0}, {'name': 'team8', 'pts': 0}, {'name': 'team9', 'pts': 0},
      {'name': 'team10', 'pts': 0}, {'name': 'team11', 'pts': 0}, {'name': 'team12', 'pts': 0},
      {'name': 'team13', 'pts': 0}, {'name': 'team14', 'pts': 0}, {'name': 'team15', 'pts': 0},
      {'name': 'team16', 'pts': 0}, {'name': 'team17', 'pts': 0}, {'name': 'team18', 'pts': 0},
      {'name': 'team19', 'pts': 0}, {'name': 'team20', 'pts': 0}]

def matchday(winner, loser, draw):
    if draw == False:
        print(f"{winner} (이)가 {loser} 에게 승리하였습니다")
        for i in vp:
            if i['name'] == winner:
                i['pts'] += 3
    if draw == True:
        print(f"{winner} 와 {loser} (이)가 무승부를 기록하였습니다")
        for i in vp:
            if i['name'] == winner or i['name'] == loser:
                i['pts'] += 1

for mdf in range(19):
    # 리그 전반부는 190경기(실제로 프리미어리그 총 경기수는 380경기)로
    # 19번의 라운드를 반복하되 라운드당 10경기를 치르는 시스템으로 정한다
    olf = []
    # 전반부에 한번 붙은 팀이 다시 만나는 일이 없도록 중복방지 리스트 생성
    mdindex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    # vp의 인덱스들
    for matchcount in range(10):
        # 한라운드 리그 경기 수(10경기)
        rd1 = random.choice(mdindex)
        # vp의 인덱스가 될 숫자중 하나 선택(mdindex중 하나 선택)
        mdindex.remove(rd1)
        # 겹치지 않도록 제거 (순열 조합 같은 느낌으로 이미 뽑은건 제거해서 다시 못뽑게함)
        rd2 = random.choice(mdindex)
        # 두번째 숫자 선택(겹칠일 없음)
        mdindex.append(rd1)
        # 계속 삭제되있으면 다음에도 안뽑히므로 다시 추가
        while {rd1, rd2} in olf:
            # 두 인덱스가 이미 선택된적이 있었을경우 반복해서 계속 랜덤으로 선택
            # 이때 인덱스가 순서와 상관이 없기때문에 set 사용
            rd1 = random.choice(mdindex)
            mdindex.remove(rd1)
            # 중복되지 않도록 삭제
            rd2 = random.choice(mdindex)
            mdindex.append(rd1)
            # 고른후 다시 추가

        mdindex.remove(rd1)
        mdindex.remove(rd2)
        # 반복문을 나온뒤 둘다 삭제
        olf.append({rd1, rd2})
        # 중복방지 리스트에 추가

        order = [rd1, rd2]
        # 승패팀 결정할 리스트에 두팀 추가
        orderr = random.choice(order)
        # rd1 과 rd2중 하나 선택(승패가 나뉠경우 승리팀과 패배팀 반반의 확률로 결정
        # 무승부시 표기되는 순서만 바뀜
        order.remove(orderr)
        # 겹치는 것을 방지하기 위해 선택된 팀을 order에서 삭제
        matchday(vp[orderr]['name'], vp[order[0]]['name'], random.choice([True, False]))
        # 처음에 선택된 팀의 이름  여기서 인덱스가 0인 이유는 요소가 두개인 order에서 하나가 삭제되어 요소가 하나밖에 안남았기 때문
for mds in range(19):
    # 리그 후반부는 190경기(실제로 프리미어리그 총 경기수는 380경기)로
    # 19번의 라운드를 반복하되 라운드당 10경기를 치르는 시스템으로 정한다
    olf = []
    # 전반부에 한번 붙은 팀이 다시 만나는 일이 없도록 중복방지 리스트 생성
    mdindex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    # vp의 인덱스들
    for matchcount in range(10):
        # 한라운드 리그 경기 수(10경기)
        rd1 = random.choice(mdindex)
        # vp의 인덱스가 될 숫자중 하나 선택(mdindex중 하나 선택)
        mdindex.remove(rd1)
        # 겹치지 않도록 제거 (순열 조합 같은 느낌으로 이미 뽑은건 제거해서 다시 못뽑게함)
        rd2 = random.choice(mdindex)
        # 두번째 숫자 선택(겹칠일 없음)
        mdindex.append(rd1)
        # 계속 삭제되있으면 다음에도 안뽑히므로 다시 추가
        while {rd1, rd2} in olf:
            # 두 인덱스가 이미 선택된적이 있었을경우 반복해서 계속 랜덤으로 선택
            rd1 = random.choice(mdindex)
            mdindex.remove(rd1)
            # 중복되지 않도록 삭제
            rd2 = random.choice(mdindex)
            mdindex.append(rd1)
            # 고른후 다시 추가

        mdindex.remove(rd1)
        mdindex.remove(rd2)
        # 반복문을 나온뒤 둘다 삭제
        olf.append({rd1, rd2})
        # 중복방지 리스트에 추가

        order = [rd1, rd2]
        # 승패팀 결정할 리스트에 두팀 추가
        orderr = random.choice(order)
        # rd1 과 rd2중 하나 선택(승패가 나뉠경우 승리팀과 패배팀 반반의 확률로 결정
        # 무승부시 표기되는 순서만 바뀜
        order.remove(orderr)
        # 겹치는 것을 방지하기 위해 선택된 팀을 order에서 삭제
        matchday(vp[orderr]['name'], vp[order[0]]['name'], random.choice([True, False]))
        # 처음에 선택된 팀의 이름  여기서 인덱스가 0인 이유는 요소가 두개인 order에서 하나가 삭제되어 요소가 하나밖에 안남았기 때문
vp.sort(key=lambda vir: vir['pts'],reverse=True)
#승점 역순으로 (큰것부터) vp 리스트 정렬(기존의 내용 필요없으므로 덮어씌우는 sort 사용)
count = 0
for i in vp:
    count += 1
    #count 하나씩 증가시키면서 등수 올림
    print(f"{count}위 : {i['name']} {i['pts']}pts")

print(f"{vp[0]['name']} 프리미어리그 우승!")
#승점 역순으로 정렬된 vp의 첫번째 요소. 즉 1위팀
print(f"{vp[17]['name']} 2부리그로 강등")
print(f"{vp[18]['name']} 2부리그로 강등")
print(f"{vp[19]['name']} 2부리그로 강등")
#마지막 3개의 요소들, 강등팀
