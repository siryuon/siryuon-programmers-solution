from itertools import combinations
from collections import defaultdict

orders = ['ABCDXE', 'ASFWB', 'CSFYD', 'ADFSE', 'XRWYZ', 'XASWYZ', 'ACDRXZC']
course = [3,4,5]

def solution(orders, course):

    result =[]
    
    course_comb = defaultdict(int)

    for i in range(len(orders)):
        for j in range(2, len(orders)):
            for k in combinations(orders[i], j):
                course_comb[tuple(sorted(k))] += 1

    course_list = []

    for size in course:
        tmp_list = []
        
        for key, value in course_comb.items():
            if len(key) == size:
                tmp_list.append(value)

        if len(tmp_list) == 0:
            continue
        
        max_size = max(tmp_list)

        for key, value in course_comb.items():
            if len(key) == size and value == max_size and value >= 2:
                course_list.append(key)

    for courses in course_list:
        result.append("".join(courses))
        
    return sorted(result)

print(solution(orders, course))
