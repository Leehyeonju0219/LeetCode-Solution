class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub('[^\w]',' ',paragraph)
                 .lower().split()
                 if word not in banned]
        
        counter = collections.Counter(words)
        max = 0
        value = ""
        for k,v in counter.items():
            if v > max:
                max = v
                value = k
                
        return value