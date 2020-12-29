from itertools import permutations

def solution(n, weak, dist):
    weakLen = len(weak)

    for i in range(weakLen):
        weak.append(weak[i] + n)

    answer = len(dist) + 1

    for i in range(weakLen):
        startPoint = [weak[j] for j in range(i, i+weakLen)]

        friend = permutations(dist, len(dist))

        for order in friend:
            friendIdx, count = 0, 1
            checkLen = startPoint[0] + order[friendIdx]

            for idx in range(weakLen):
                if startPoint[idx] > checkLen:
                    count += 1
                    if count > len(order):
                        break
                    friendIdx += 1
                    checkLen = order[friendIdx] + startPoint[idx]
            answer = min(answer, count)

    if answer > len(dist):
        return -1

    return answer


n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

print(solution(n, weak, dist))
