class Solution:
    # 2942. 查找包含给定字符的单词
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, s in enumerate(words) if x in s]