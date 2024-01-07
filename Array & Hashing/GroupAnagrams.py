class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        combined_arr = []
        for s in strs:
            x = ''.join(sorted(s))
            combined_arr.append((x, s))
        hash_map = {}
        for i in combined_arr:
            if i[0] in hash_map:
                hash_map[i[0]].append(i[1])
            else:
                hash_map[i[0]] = [i[1]]
        return list(hash_map.values())
