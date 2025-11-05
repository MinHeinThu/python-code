# Selection Sort
# Time: O(n^2), Space 0(1)

# Selection sort contain unsort and sort part
nums =  [2,7,11,15]
target = 9
#[6, 2, 5, 3, 9] 
class Solution:
    def twoSum(self, nums: list[int], target: int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None  # Return None if no solution is found

if __name__ == "__main__":
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)
                    