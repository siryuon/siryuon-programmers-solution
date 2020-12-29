def check(result):
    for x, y, kind in result:
        if kind == 0:
            if y == 0 or [x-1, y, 1] in result or [x, y, 1] in result or [x, y-1, 0] in result:
                continue
            else:
                return False
        elif kind == 1:
            if [x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result):
                continue
            else:
                return False

    return True
            
def solution(n, build_frame):
    answer = []

    for work in build_frame:
        x, y, kind, do = work

        if do == 1:
            answer.append([x, y, kind])
            if check(answer) is False:
                answer.remove([x, y, kind])
        elif do == 0:
            answer.remove([x, y, kind])
            if check(answer) is False:
                answer.append([x, y, kind])
    answer.sort()
    return answer
