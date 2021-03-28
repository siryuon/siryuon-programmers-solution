def solution(play_time, adv_time, logs):

    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)

    time_table = [0 for i in range(play_time + 1)]

    for log in logs:
        start, end = log.split("-")
        start = time_to_sec(start)
        end = time_to_sec(end)
        for i in range(start, end+1):
            time_table[i] += 1
    print(time_table)
    most_view = 0
    viewers_list = []

    for i in range(adv_time - 1, play_time):
        viewers = sum(time_table[i - adv_time : i + 1])
        most_view = max(most_view, viewers)
        viewers_list.append(most_view)
        viewers_list.append(sec_to_time(i))
        print(viewers, sec_to_time(i))
    adv_end_time = viewers_list[viewers_list.index(most_view)+1]
    adv_end_time = time_to_sec(adv_end_time)

    result = adv_end_time - adv_time

    return sec_to_time(result) 


def time_to_sec(time):
    h, m, s = time.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)

def sec_to_time(sec):
    h = sec // 3600
    h = "0" + str(h) if h < 10 else str(h)

    sec = sec % 3600
    m = sec // 60
    m = "0" + str(m) if m < 10 else str(m)

    sec = sec % 60
    s  ="0" + str(sec) if sec < 10 else str(sec)

    return h + ":" + m + ":" + s

play_time = "00:10:00"
adv_time = "00:02:30"
logs=["00:01:22-00:02:38", "00:05:29-00:07:43"]
#logs= ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
print(solution(play_time, adv_time, logs))
359999
