class Solution(object):
    def licenseKeyFormatting(self, S, K):

        S = S.replace('-','')

        mod = len(S)%K
        if not mod:
            ans = ''
        else:
            ans = S[:mod]+'-'

        i = mod
        while i < len(S):
            ans += S[i:i+K]+'-'
            i += K
        res = ans[:-1]
        #print(ans)
        print(ans[:-1])
        return res.upper()
        
