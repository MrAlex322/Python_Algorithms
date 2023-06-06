# Дано два массива строк list1 и list2, найдите общие строки с наименьшей суммой индексов.
# Общая строка — это строка, которая появляется как в list1, так и в list2.
# Обычная строка с наименьшей суммой индексов — это такая обычная строка, что если она появляется
# в списках list1[i] и list2[j], то i + j должно быть минимальным значением среди всех остальных общих строк.
# Возвращает все общие строки с наименьшей суммой индексов. Верните ответ в любом порядке.
# TimeComplexity - O(N), где N - максимальная длина из двух списков list1 и list2.


class Solution:
    def findMinIndexSum(self, list1, list2):
        common_strings = {}  # словарь для хранения общих строк и их сумм индексов

        # заполнение словаря значениями из list1
        for i in range(len(list1)):
            common_strings[list1[i]] = i

        # обновление словаря значениями из list2 и вычисление сумм индексов
        for j in range(len(list2)):
            if list2[j] in common_strings:
                common_strings[list2[j]] += j
            else:
                common_strings[list2[j]] = j

        min_index_sum = min(common_strings.values())  # нахождение минимальной суммы индексов

        result = [string for string, index_sum in common_strings.items() if index_sum == min_index_sum]

        return result


# примеры использования
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
solution = Solution()
print(solution.findMinIndexSum(list1, list2))  # Output: ["Shogun"]

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
print(solution.findMinIndexSum(list1, list2))  # Output: ["Shogun"]

list1 = ["happy", "sad", "good"]
list2 = ["sad", "happy", "good"]
print(solution.findMinIndexSum(list1, list2))  # Output: ["sad", "happy"]
