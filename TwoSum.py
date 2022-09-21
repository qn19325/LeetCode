def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for idx, val in enumerate(nums):
            toSearch = target - val
            if toSearch in hash_table.keys():
                return [idx, hash_table[toSearch]]
            hash_table[val] = idx