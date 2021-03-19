class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []
    
        def helper(nums_available: List[int], current_list: List[int]):
            if len(nums_available) == 0:
                permutations.append(current_list)
                return
            else:
                for i in range(len(nums_available)):
                    helper(nums_available[:i]+nums_available[i+1:], current_list+[nums_available[i]])
                
        helper(nums, [])
        return permutations