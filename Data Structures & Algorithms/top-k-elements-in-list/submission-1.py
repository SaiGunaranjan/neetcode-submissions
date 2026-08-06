class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        import numpy as np

        uniq_vals, counts = np.unique(np.array(nums),return_counts=True)

        ind = np.argsort(-counts)

        arr = list(uniq_vals[ind][0:k])

        return arr

        