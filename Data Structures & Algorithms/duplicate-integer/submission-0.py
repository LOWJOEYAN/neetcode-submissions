class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for i in nums:
            if i in hash_table:
                hash_table[i] += 1

            else:
                hash_table[i] = 1

        for key in hash_table:
            if hash_table[key] > 1:
                return True
        
        return False

find = Solution()
nums=[1,2,3,3]
find.hasDuplicate(nums)



    

            
        