class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people = sorted(people)
        len_arr = len(people)
        lp = 0
        rp = len_arr - 1
        min_boats_req = 0
        while lp < rp:
            if people[lp] + people[rp] > limit:
                rp -= 1
            else:
                lp += 1
                rp -= 1
            min_boats_req += 1
        if lp == rp:
            min_boats_req += 1

        return min_boats_req