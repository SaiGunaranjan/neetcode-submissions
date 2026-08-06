class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums_sort = sorted(nums)
        len_arr = len(nums)
        prev_val = -1e6
        triplet_list = []
        for i in range(0,len_arr-2):
            if nums_sort[i] == prev_val:
                continue
            else:
                prev_val = nums_sort[i]
                lp = i+1
                rp = len_arr - 1
                two_sum = -nums_sort[i]
                prev_lp_val = -1e6
                prev_rp_val = 1e6
                while lp < rp:
                    if nums_sort[lp] == prev_lp_val:
                        lp += 1
                        continue
                    if nums_sort[rp] == prev_rp_val:
                        rp -= 1
                        continue
                    if nums_sort[lp] + nums_sort[rp] > two_sum:
                        prev_rp_val = nums_sort[rp]
                        rp -= 1
                    elif nums_sort[lp] + nums_sort[rp] < two_sum:
                        prev_lp_val = nums_sort[lp]
                        lp += 1
                    else:
                        triplet_list.append([nums_sort[i],nums_sort[lp],nums_sort[rp]])
                        prev_lp_val = nums_sort[lp]
                        prev_rp_val = nums_sort[rp]
                        lp += 1
                        rp -= 1

        return triplet_list


        