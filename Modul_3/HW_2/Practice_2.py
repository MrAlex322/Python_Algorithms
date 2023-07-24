# Дан массив целых чисел nums, содержащий n + 1 целых чисел, где каждое целое число находится в диапазоне
# [1, n] включительно. В nums есть только одно повторяющееся число, верните это повторяющееся число.
# Нужно решить задачу, не изменяя массив nums и не используя дополнительную память.
# time complexity - O(n) и memory complexity = O(1)


def findDuplicate(nums: list) -> int:
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    fast = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


nums = [1, 3, 2, 4, 2]
print(findDuplicate(nums))