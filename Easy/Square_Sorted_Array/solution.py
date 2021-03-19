class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            nums[0] = nums[0]**2
            return nums
        output = []
        left_index = 0
        right_index = len(nums) - 1
        while left_index != right_index:
            left = abs(nums[left_index])
            right = abs(nums[right_index])
            if left >= right:
                output.append(left**2)
                left_index += 1
            else:
                output.append(right**2)
                right_index -= 1

        output.append(nums[left_index]**2)
        return output[::-1]