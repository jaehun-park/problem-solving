from datetime import datetime

def convert(melody):
    melody = melody.replace('A#', 'a')
    melody = melody.replace('C#', 'c')
    melody = melody.replace('D#', 'd')
    melody = melody.replace('F#', 'f')
    melody = melody.replace('G#', 'g')
    
    return melody


def play_time(start, end):
    start_time = datetime.strptime(start,"%H:%M")
    end_time = datetime.strptime(end,"%H:%M")
    time_interval = end_time - start_time
    
    return time_interval.seconds // 60


def played_melody(melody, time):
    music_len = len([note for note in melody if note.isalpha()])
    played = time // music_len
    rest = time % music_len
    
    result = melody * played + melody[:rest]

    return result
    
    
def solution(m, musicinfos):
    matched = []
    m = convert(m)
    for musicinfo in musicinfos:
        start_time, end_time, title, melody = musicinfo.split(',')
        melody = convert(melody)
        time = play_time(start_time, end_time)
        
        if m in played_melody(melody, time):
            matched.append([title, time])
    
    if not matched:
        return "(None)"
    
    matched.sort(key=lambda x:x[1], reverse=True)
    
    return matched[0][0]