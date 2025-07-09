class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        table = defaultdict(list)


        for word in strs:
            count = [0] * 26

            for letter in word:
                count[ord(letter) - ord('a')] += 1
            
            table[tuple(count)].append(word)
        
        return list(table.values())