class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        answer = [0] * 2
        count = 0
        for i in nums:
            if i in hash_map:
                hash_map[i] = count
                count += 1
                continue
            hash_map[i] = count
            count += 1
        print(hash_map)

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash_map and hash_map[difference] != i:
                answer = [i, hash_map[difference]]
                break

        return answer


                

        
        