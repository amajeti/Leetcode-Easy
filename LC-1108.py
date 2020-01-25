class Solution(object):
    def defangIPaddr (self, a): 
        return ''.join(['[.]' if _a == '.' else _a for _a in a])


