# Для заданной строки s найдите длину самой длинной подстроки без повторяющихся символов. Верните саму строку
# Например:
# s = abcabcbb - ответ: abc
# s = pwwkew - ответ: wke
# s = bbbbb - ответ: b


class Anagrams:
    def find_longest_substring(self, s):
        if not s:
            return ""

        start = 0
        end = 0
        max_len = 1
        max_substr = s[0]
        substr = {}

        for i in range(len(s)):
            if s[i] in substr and substr[s[i]] >= start:
                start = substr[s[i]] + 1

            end = i
            substr[s[i]] = i

            if end - start + 1 > max_len:
                max_len = end - start + 1
                max_substr = s[start:end+1]

        return max_substr