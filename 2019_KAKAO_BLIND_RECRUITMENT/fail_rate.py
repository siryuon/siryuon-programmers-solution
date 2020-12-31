from collections import Counter

def solution(N, stages):
    failureRate = []
    answer = []
    setStages = Counter(stages)

    for stage in range(0, N):
        tryer = 0
        finisher = 0

        for key in setStages.keys():
            if key - 1 == stage:
                tryer = tryer + setStages[key]   
            elif key - 1 > stage:
                finisher = finisher + setStages[key]

        if (tryer + finisher) != 0:
            failureRate.append([stage+1, tryer/(tryer+finisher)])
        else:
            failureRate.append([stage+1 , 0])


    for i in range(0, N):
        answer.append(sorted(failureRate, key = lambda failure: failure[1], reverse = True)[i][0])
        
    return answer
