class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for value in strs:
            key = ''.join(sorted(value))
            anagram_map[key].append(value)

        return list(anagram_map.values())