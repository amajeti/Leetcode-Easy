class Solution(object):
    def plusOne(self, a):
        s=''
        res = []
        for i in a:
            s += str(i)

        in_s = int(s)
        in_s += 1
        in_s = str(in_s)

        for j in (in_s):
            res.append(int(j))

        return res
        
