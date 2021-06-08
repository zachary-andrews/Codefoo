from typing import List

class Sum:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def dfs(total,path,index):
            # success
            if total == target:
                results.append(path.copy())
                return
            ## fail
            if index >= len(candidates) or total > target:
                return

            ## include
            path.append(candidates[index])
            dfs(total+candidates[index],path,index)
            #exclude
            path.pop()
            dfs(total,path,index+1)
    
        dfs(0,[],0)
        return results