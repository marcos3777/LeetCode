#884-Uncommon Words from Two Sentences
from typing import Counter, List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split() 
        words2 = s2.split()
        wordCount = Counter(words1 + words2)
        uncommonWords = []

        for word in wordCount:
            if wordCount[word] == 1:
                uncommonWords.append(word)

        return uncommonWords
    