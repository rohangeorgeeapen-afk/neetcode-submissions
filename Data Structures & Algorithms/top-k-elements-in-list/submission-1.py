class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        grouped = {}
        for num in nums:
            if num not in grouped:
                grouped[num] = []
            grouped[num].append(num)

        sorted_nums = sorted(grouped.keys(), key=lambda num: len(grouped[num]), reverse=True)

        return sorted_nums[:k]