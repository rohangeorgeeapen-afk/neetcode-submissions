class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped={}
        for word in strs:
            sortedword=''.join(sorted(word))
            if sortedword not in grouped:
                grouped[sortedword]=[]
            grouped[sortedword].append(word)
        return list(grouped.values())