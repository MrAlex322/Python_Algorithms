# Даны массив arr, target число
# Известно, что массив отсортирован в порядке возрастания. вернуть Нужно найти индекс, если target найден в arr.
# Если нет, вернуть индекс туда, где он был бы, если бы он был вставлен по порядку.
# Примеры:
# arr = [1,3,5,6], target = 5
# Ответ: 2
# arr = [1,3,5,6], target = 2
# Ответ: 1
# time complexity - O(log n)
# memory complexity - O(1).

class BinarySearch:
    def search_insert(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


# Пример использования
arr = [2, 8, 9, 11]
target = 9

bs = BinarySearch()
result = bs.search_insert(arr, target)
print(result)



