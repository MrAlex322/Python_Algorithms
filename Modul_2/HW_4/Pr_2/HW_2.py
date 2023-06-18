# Дано два массива строк list1 и list2, найдите общие строки с наименьшей суммой индексов.
# Общая строка — это строка, которая появляется как в list1, так и в list2.
# Обычная строка с наименьшей суммой индексов — это такая обычная строка, что если она появляется
# в списках list1[i] и list2[j], то i + j должно быть минимальным значением среди всех остальных общих строк.
# Возвращает все общие строки с наименьшей суммой индексов. Верните ответ в любом порядке.
# TimeComplexity - O(N), где N - максимальная длина из двух списков list1 и list2.
# Memory complexity - (len(list1))


class Solution:
    def findMinIndexSum(self, list1, list2):
        common_strings = {}

        for i_el, element in enumerate(list1):
            common_strings[element] = i_el

        min_index_sum = float('inf')
        result = []

        for j_el, element in enumerate(list2):
            if element in common_strings:
                index_sum = j_el + common_strings[element]
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    result = [element]
                elif index_sum == min_index_sum:
                    result.append(element)

        return result


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
solution = Solution()
print(solution.findMinIndexSum(list1, list2))

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
print(solution.findMinIndexSum(list1, list2))

list1 = ["happy", "sad", "good"]
list2 = ["sad", "happy", "good"]
print(solution.findMinIndexSum(list1, list2))
