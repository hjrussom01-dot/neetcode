class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for str in strs:
                sort = "".join(sorted(str))
                if sort in ans:
                        ans[sort].append(str)
                else:
                        ans[sort] = [str]
        return list(ans.values())