def check(place):
    place = ['XXXXXXX'] + [row + 'XX' for row in place] + ['XXXXXXX'] * 2
    for i in range(1,6):
        for j in range(5):
            if place[i][j] != 'P': continue
            if 'P' in (place[i+1][j], place[i][j+1]): return 0
            if place[i+1][j] == 'O' and place[i+2][j] == 'P': return 0
            if place[i][j+1] == 'O' and place[i][j+2] == 'P': return 0
            if 'O' in (place[i][j+1], place[i+1][j]) and place[i+1][j+1] == 'P': return 0
            if 'O' in (place[i-1][j], place[i][j+1]) and place[i-1][j+1] == 'P': return 0
    return 1


def solution(places):
    return list(map(check, places))