def solution(info, query):
    person_list = []
    condition_list = []
    
    for person in info:
        person = person.split(" ")
        person_list.append(person)

    for condition in query:
        condition = condition.replace('and', '').split(" ")
        condition_list.append(condition)
    result = set()
    result = set(person_list) & set(condition_list)

    print(result)

    print(person_list)
    print(condition_list)
'''
    for conditions in condition_list:
        for person in person_list:
            for condition in conditions:
'''


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]


print(solution(info, query))
'''
for person in info:
    print (person.split(" "))

print("-------------------------")

for condition in query:
    condition = condition.split(" ")

    for a in condition:
        if a != "and":
            print(a)
'''
