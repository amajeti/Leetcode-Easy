import numpy as np
class Solution(object):
    def twoSum(self, nums, target):
        nums_dup = nums[:] 
        nums.sort()
        res = []
        n = len(nums)
        lhs = 0
        rhs = n-1
        while lhs < rhs:
            sum1 = nums[lhs] + nums[rhs]
            if sum1 == target:
                if nums_dup == nums:
                    res.append(lhs)
                    res.append(rhs)
                    return res
                else:
                    if nums[lhs] == nums[rhs]:
                        values = np.array(nums_dup)
                        l = np.where(values == nums[lhs])[0]
                        res.append(l[0])
                        res.append(l[-1])
                    else:
                        res.append(nums_dup.index(nums[lhs]))
                        res.append(nums_dup.index(nums[rhs]))
                    return res

            elif sum1< target:
                lhs += 1
            else:
                rhs -= 1

        return res
    
