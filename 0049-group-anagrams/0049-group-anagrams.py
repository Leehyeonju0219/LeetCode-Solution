from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str = defaultdict(list)
        for string in strs:
            str_list = list(string)
            sorted_str[''.join(sorted(str_list))].append(str_list)
        
        answer = []
        for k,v in sorted_str.items():
            word_set = []
            for word in v:
                word_set.append(''.join(word))
            answer.append(word_set)
        
        return answer
            