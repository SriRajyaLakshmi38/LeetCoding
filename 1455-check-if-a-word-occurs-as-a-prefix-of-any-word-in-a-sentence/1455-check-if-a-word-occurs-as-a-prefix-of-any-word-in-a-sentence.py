class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        lis = sentence.split()
        for i,w in enumerate (lis):
            if w.startswith(searchWord):
                return i+1
        return -1    
                    