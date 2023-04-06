#Дан массив строк strs, требуется сгруппировать анаграммы вместе. 
#Например: 
#strs = ["eat","tea","tan","ate","nat","bat"] - 
#ответ: [["bat"],["nat","tan"],["ate","eat","tea"]]


class AnagramGrouper:
    def group_anagrams(self):
        s = input("Введите строку: ")
        d = {}
        for word in s.split():
            key = ''.join(sorted(word))
            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]
        return list(d.values())


anagram_grouper = AnagramGrouper()
result = anagram_grouper.group_anagrams()
print(result)
