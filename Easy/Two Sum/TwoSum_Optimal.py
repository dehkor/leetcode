class TwoSum_Optimal:
    def twoSum(nums: list, target: int) -> list:
        solution_hash = {}
        for i in range(len(nums)):
            remainder_index = solution_hash.get(target-nums[i])
            if(remainder_index != None and remainder_index != i):
                return [remainder_index, i]
            solution_hash[nums[i]] = i
