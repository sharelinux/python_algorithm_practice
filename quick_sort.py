def quickSort(nums):
    """快速排序法"""
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]
    left = [l for l in nums if l < pivot]
    middle = [m for m in nums if m == pivot]
    right = [r for r in nums if r > pivot]

    return quickSort(left) + middle + quickSort(right)


aList = [1, 9, 3, 7, 4, 5, 8, 2, 6]
print("quickSort: %s" % quickSort(aList))
