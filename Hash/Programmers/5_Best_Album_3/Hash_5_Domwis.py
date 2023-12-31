# Quiz Link: https://school.programmers.co.kr/learn/courses/30/lessons/42579

import operator
def solution(genres, plays):
    answer = []
    songs = dict()
    for i in range(len(genres)):
        if genres[i] in songs:
            songs[genres[i]].append((i,plays[i]))
        else:
            songs[genres[i]] = [(i,plays[i])]
    
    play = dict()
    for i in songs:
        songs[i] = sorted(songs[i], key = operator.itemgetter(1),reverse = True)
        play_ = 0
        for song in songs[i]:
            play_ += song[1]
        play[i] = play_

    a = sorted(play.items(), key = operator.itemgetter(1), reverse = True)
    play = dict(a)
    
    for i in play:
        song = songs[i]
        if len(song) == 1:
            answer.append(song[0][0])
        else:
            answer.append(song[0][0])
            answer.append(song[1][0])
    return answer