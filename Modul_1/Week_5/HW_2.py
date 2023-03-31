# Данно строка и слово, требуется посчитать количество анаграмм слова в строке

# s = input("word")
# keys = []
# for i in range(0, len(s)):
#     keys.append(i)
# print(keys)
#
# dictionary = {}
#
# for i in range(len(s)):
#     dictionary[keys[i]] = s[i]
#
# print(dictionary)
#
# str_lst = "aabaabaa"
#
#
# # def sliding_window(elements, window_size):
# #     count = 0
# #     if len(elements) <= window_size:
# #         return elements
# #     for i in range(len(elements)):
# #         for values in dictionary.values():
# #             if values == elements[i]:
# #                 count += 1
# #                 break
# #     print(count)
#
# def sliding_window(elements, window_size):
#     count = 0
#     best_count = 0
#     if len(elements) <= window_size:
#         return elements
#     for i in range(len(elements) - window_size + 1):
#         for values in dictionary.values():
#             if values in elements[i:i + window_size]:
#                 count += 1
#                 if count == 4:
#                     best_count += 1
#                     count = 0
#             else:
#                 count = 0
#     print(best_count)
#
# sliding_window(str_lst, len(s))


word = sorted(input("Введите слово: "))

str_lst = "forxxorfxdofr"


def sliding_window(elements, window_size):
    count = 0
    if len(elements) <= window_size:
        return elements
    for i in range(len(elements) - window_size + 1):
            if word == sorted(elements[i:i + window_size]):
                count+=1
    print(count)


sliding_window(str_lst, len(word))


def find_anagrams(s: str, p: str) -> List[int]:
    p_dict = {}
    s_dict = {}
    result = []

    # Fill the p_dict dictionary with the frequency of each character in p
    for c in p:
        p_dict[c] = p_dict.get(c, 0) + 1

    # Fill the s_dict dictionary with the frequency of each character in the first window of size len(p)
    for c in s[:len(p)]:
        s_dict[c] = s_dict.get(c, 0) + 1

    # Check if the first window is an anagram of p
    if s_dict == p_dict:
        result.append(0)

    # Slide the window and update the s_dict dictionary
    for i in range(1, len(s) - len(p) + 1):
        # Remove the frequency of the leftmost character from the s_dict dictionary
        if s_dict[s[i - 1]] == 1:
            del s_dict[s[i - 1]]
        else:
            s_dict[s[i - 1]] -= 1

        # Add the frequency of the character to the right of the window to the s_dict dictionary
        s_dict[s[i + len(p) - 1]] = s_dict.get(s[i + len(p) - 1], 0) + 1

        # Check if the current window is an anagram of p
        if s_dict == p_dict:
            result.append(i)

    return result

#
# def getCountOccurances(text, word):
#     wHeap = [0] * 26
#     textHeap = [0] * 26
#     start = 0
#     count = 0
#
#     for c in word:
#         wHeap[ord(c) - ord('a')] += 1
#
#     for i in range(len(text)):
#         textHeap[ord(text[i]) - ord('a')] += 1
#         if (i - start + 1) == len(word):
#             if textHeap == wHeap:
#                 count += 1
#
#             textHeap[ord(text[start]) - ord('a')] -= 1
#             start += 1
#
#     return count