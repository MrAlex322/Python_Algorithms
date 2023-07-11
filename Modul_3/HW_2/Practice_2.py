def findDuplicate(nums):
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