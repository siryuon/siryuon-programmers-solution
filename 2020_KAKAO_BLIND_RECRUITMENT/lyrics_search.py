from collections import defaultdict

def insert(trie, word):
    for char in word:
        if char not in trie:
            trie[char] = [dict(), 0]
        trie[char][1] += 1
        trie = trie[char][0]

def find(word, trie):
    count = 0

    for char in word:
        if char == '?':
            return count
        if char not in trie:
            return 0
        count = trie[char][1]
        trie = trie[char][0]
    
def solution(words, queries):
    maxLen = 0
    result = [0] * len(queries)
    wordDic = defaultdict(list)
    
    for word in words:
        if maxLen < len(word):
            maxLen = len(word)

    for word in words:
        wordDic[len(word)].append(word)
    
    trieList = [[dict(), dict()] for _ in range(maxLen+1)]

    for word in words:
        wordLen = len(word)
        trie = trieList[wordLen]
        insert(trie[0], word)
        insert(trie[1], word[::-1])

    for idx, query in enumerate(queries):
        wordLen = len(query)
        wildCount = 0
    
        for char in query:
            if char == '?':
                wildCount += 1
            
        if wordLen > maxLen:
            result[idx] = 0
            continue
        trie = trieList[wordLen]
        if wildCount == len(query):
            result[idx] = len(wordDic[len(query)])
        elif query[0] != '?':
            result[idx] = find(query, trie[0])
        else:
            result[idx] = find(query[::-1], trie[1])

    return result
