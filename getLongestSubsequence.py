class Solution:
    # 2900. 最长相邻不相等子序列 I
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        ans = []
        for i, x in enumerate(groups) :
            if i == n - 1 or x != groups[i+1]:
                ans.append(words[i])
        return ans