def split(p):
    num = 0
    bucket = []

    for idx, value in enumerate(p):
        if value == ')':
            num -= 1
        elif value == '(':
            num += 1

        if num == 0:
            return idx

def right(p):
    bucket = []

    for bracket in p:
        if bracket == '(':
            bucket.append(bracket)
        else:
            if len(bucket) == 0:
                return False
            bucket.pop()

    if len(bucket) == 0:
        return True
    else:
        return False
        
def solution(p):
    if p == "" or right(p):
        return p

    u, v  = p[:split(p)+1], p[split(p)+1:]

    if right(u):
        string = solution(v)
        return u + string
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            elif u[i] == ')':
                u[i] = '('

        answer += "".join(u)
    return answer
