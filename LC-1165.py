class Solution(object):
    def calculateTime(self, keyboard, word):
        li = []
        dic= {keyboard[i]:i for i in range(26)}
        
        res = 0
        cur = 0
        
        for c in word:
            res += abs(dic[c] - cur)
            cur = dic[c]

        return res
