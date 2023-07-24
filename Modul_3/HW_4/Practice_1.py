#Дан целочисленный массив nums и целое число k, вернуть k наиболее часто встречающихся элементов.
#Вы можете вернуть ответ в любом порядке. Time complexity не должна превышать O(n*logn)


from collections import Counter

def most_frequent(nums, k):
    counter = Counter(nums)
    max_freq = max(counter.values())
    frequency_list = [[] for _ in range(max_freq+1)]

    for num, freq in counter.items():
        frequency_list[freq].append(num)

    result = []
    for i in range(max_freq, 0, -1):
        if len(result) >= k:
            break
        result.extend(frequency_list[i])

    return result[:k]


print(most_frequent([1], 1))





