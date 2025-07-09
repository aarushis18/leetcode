from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        table = defaultdict(list)

        for word in strs:
            table[str(sorted(word))].append(word)
        
        final = []
        for key in table:
            final.append(table[key])
        
        return final 