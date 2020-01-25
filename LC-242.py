class Solution(object):
    def isAnagram(self, s, t):

        se = ''.join(sorted(s))
        te = ''.join(sorted(t))
        boo = False
        if te == se:
            boo = True
        else:
            boo = False
        return boo
