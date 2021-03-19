class Solution:
    def trap(self, height: List[int]) -> int:
        water_levels = []
        highpoint = 0
        if len(height) < 3:
            return 0
        for i,h in enumerate(height):
            if h >= highpoint:
                highpoint = h
                print("highpoint set")
            else:
                if h < highpoint and h < max(height[i:]):
                    water_levels.append(min(highpoint,max(height[i:]))-h)
                    print("collect water")
                else:
                    highpoint = h
                    print("reset height")  
        return sum(water_levels)