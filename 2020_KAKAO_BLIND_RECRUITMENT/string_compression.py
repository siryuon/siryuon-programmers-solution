def solution(s):
    answer = 1000

    if len(s) == 1:
        return 1

    for size in range(1, int(len(s) / 2) + 1):
        count = 0
        before_word = ""
        
        for i in range(0, len(s)+1, size):
            if before_word[-size:] == s[i:i+size]:
                count += 1

            else:
                if count > 1:
                    before_word += str(count) + s[i:i+size]

                else:
                    before_word += s[i:i+size]
                    
                count = 1
                
        if answer > len(before_word):
            answer = len(before_word)
        
    return answer
