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



# 전반부 중복방지
for mdf in range(10):
    olf = []
    # 리그 전반부는 190경기(실제로 프리미어리그 총 경기수는 380경기)로 10번 반복하되 라운드당 9경기를 치르는 시스템으로 정한다
    mdindex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    for matchcount in range(9):
        # 한라운드 리그 경기 수(9경기)
        rd1 = random.choice(mdindex)
        mdindex.remove(rd1)
        rd2 = random.choice(mdindex)
        mdindex.append(rd1)

        # 두 인덱스 선택
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
        orderr = random.choice(order)
        order.remove(orderr)
        matchday(vp[orderr]['name'], vp[order[0]]['name'], random.choice([True, False]))
for mds in range(10):
    olf = []
    # 리그 전반부는 190경기(실제로 프리미어리그 총 경기수는 380경기)로 10번 반복하되 라운드당 9경기를 치르는 시스템으로 정한다
    mdindex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    for matchcount in range(9):
        # 한라운드 리그 경기 수(9경기)
        rd1 = random.choice(mdindex)
        mdindex.remove(rd1)
        rd2 = random.choice(mdindex)
        mdindex.append(rd1)

        # 두 인덱스 선택
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
        orderr = random.choice(order)
        order.remove(orderr)
        matchday(vp[orderr]['name'], vp[order[0]]['name'], random.choice([True, False]))
