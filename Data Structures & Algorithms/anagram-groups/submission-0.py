class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang_dict = {}
        
        for i in range(len(strs)):
            has_ang = False
            for key in ang_dict:
                if self._is_anagram(key, strs[i]):
                    ang_dict[key].append(strs[i])
                    has_ang = True
                    break
            if not has_ang:
                ang_dict[strs[i]] = [strs[i]]
        return list(ang_dict.values())

    def _is_anagram(self, a: str, b: str) -> bool:
        char_count = {}
        for c in a:
            if c in char_count:
                char_count[c] = char_count[c] + 1
            else:
                char_count[c] = 1
        
        for c in b:
            if c in char_count and char_count[c] > 0:
                char_count[c] = char_count[c] - 1
            else:
                return False
        
        for val in char_count.values():
            if val != 0:
                return False

        return True