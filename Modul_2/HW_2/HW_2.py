# Дан массив строк strs, требуется сгруппировать анаграммы вместе.
# Например
# strs = [eat,tea,tan,ate,nat,bat] -
# ответ [[bat],[nat,tan],[ate,eat,tea]]
#
# strs = []
# ответ [[]]
#
# strs = [a]
# ответ [[a]]

from collections import defaultdict
from typing import List

class AnagramGrouper:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        ht = defaultdict(list)
        for s in strs:
            # create dictionary for current string
            current_ht = [0] * 26
            for c in s:
                current_ht[ord(c) - ord('a')] += 1

            # check if current string belongs to an existing group
            found = False
            for i, (h, group) in enumerate(ht.items()):
                if h == tuple(current_ht):
                    group.append(s)
                    found = True
                    break

            # create new group if current string doesn't belong to any existing group
            if not found:
                ht[tuple(current_ht)] = [s]
                groups.append(ht[tuple(current_ht)])

        return groups


anagram_grouper = AnagramGrouper()
strs = ["eat","tea","tan","ate","nat","bat"]
groups = anagram_grouper.group_anagrams(strs)
print(groups)
