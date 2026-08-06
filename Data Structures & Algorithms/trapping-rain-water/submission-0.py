class Solution:
    def trap(self, height: List[int]) -> int:

        len_arr = len(height)
        max_height_left = []
        max_height_right = []
        # Max height from left
        left_max = 0
        for val in height:
            left_max = max(left_max,val)
            max_height_left.append(left_max)
        
        right_max = 0
        for val in height[-1::-1]:
            right_max = max(right_max,val)
            max_height_right.append(right_max)

        water_stored = 0
        for i in range(len_arr):
            limit_height = min(max_height_left[i], max_height_right[len_arr-i-1])
            if limit_height > height[i]:
                water_stored += (limit_height - height[i])

        return water_stored


        