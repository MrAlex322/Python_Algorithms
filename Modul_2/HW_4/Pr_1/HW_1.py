# Мы определяем гармоничный массив как массив, в котором разница между его максимальным значением и
# минимальным значением равна ровно 1.
#
# Дан целочисленный массив nums, вернуть длину его самой длинной гармоничной подпоследовательности
# среди всех возможных подпоследовательностей.
#
# Подпоследовательность массива — это последовательность, которая может быть получена
# из массива путем удаления некоторых элементов или их отсутствия без изменения порядка оставшихся элементов.
#TimeComplexity - O(n)

from collections import Counter


class HarmonicSubsequence:
    def findLHS(self, nums):
        freq = Counter(nums)
        max_length = 0

        for num in nums:
            if num + 1 in freq:
                length = freq[num] + freq[num + 1]
                max_length = max(max_length, length)

        return max_length


# Примеры использования
h = HarmonicSubsequence()

nums1 = [1, 3, 2, 2, 5, 2, 3, 7]
print(h.findLHS(nums1))

nums2 = [1, 2, 3, 4]
print(h.findLHS(nums2))