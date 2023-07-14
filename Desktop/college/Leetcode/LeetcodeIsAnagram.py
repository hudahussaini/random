def isAnagram(s: str, t: str):
        myDict = {}
        for char in s:
            if char in myDict:
                num = myDict[char]['s']
                myDict[char]['s'] += 1
                continue
            myDict[char] = {}
            myDict[char]['s'] = 0
        for char in t:
            if char not in myDict:
                return False
            elif 't' in myDict[char]:
                myDict[char]['t'] += 1
            else:
                myDict[char]['t'] = 0
        for key in myDict:
            if 's' in myDict[key] and 't' in myDict[key] and myDict[key]['s'] != myDict[key]['t']:
                return False
            elif ('s' in myDict[key] and 't' not in myDict[key]) or ('s' not in myDict[key] and 't' in myDict[key]):
                return False
            else:
                continue
        return True

print(isAnagram('anagram', 'nagaram'))