# Для заданной строки s найдите длину самой длинной подстроки без повторяющихся символов. Верните саму строку
# Например:
# s = abcabcbb - ответ: abc
# s = pwwkew - ответ: wke
# s = bbbbb - ответ: b

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
