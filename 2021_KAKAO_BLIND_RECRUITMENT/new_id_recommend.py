id_list = ['...!@BaT#*..y.abcdefghijklm', 'z-+.^.', '=.=', '123_.def', 'abcdefghijklmn.p']

available_character = ['-', '_', '.']

def solution(new_id):

    new_id = new_id.lower()
    new_id = list(new_id)

    tmp_list=[]
    
    for char in new_id:
        if char.isdigit() or char.isalpha() or char in available_character:
            tmp_list.append(char)
        else:
            continue
    new_id = tmp_list[:]     
    tmp_list = []

    while new_id:
        char = new_id.pop(0)
        if len(tmp_list) == 0:
            tmp_list.append(char)
        else:
            if char == '.' and tmp_list[-1] == '.':
                tmp_list.pop()
                tmp_list.append(char)
            else:
                tmp_list.append(char)

    new_id = tmp_list[:]

    while new_id:
        if new_id[0] == '.':
            new_id.pop(0)
        elif new_id[-1] == '.':
            new_id.pop()
        else:
            break

    if len(new_id) == 0:
        new_id.append('a')

    new_id = new_id[0:15]
    if new_id[-1] == '.':
        new_id.pop()

    while new_id:
        if len(new_id) <= 2:
            new_id.append(new_id[-1])
        else:
            break
        
        
    new_id = ''.join(new_id)

    return new_id


for new_id in id_list:
    print(solution(new_id))

