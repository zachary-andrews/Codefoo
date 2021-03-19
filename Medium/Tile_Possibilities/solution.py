class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        combos = set() 
        
        def recursion(current_string: str, remaining_tiles: str):
            if len(remaining_tiles) == 0:
                combos.add(current_string)
                return
            
            
            combos.add(current_string)
            for i in range(len(remaining_tiles)):
                recursion(current_string + remaining_tiles[i], remaining_tiles[:i] +  remaining_tiles[i+1:])
        
        recursion("",tiles)
        print(combos)
        return len(combos)-1