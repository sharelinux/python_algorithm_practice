def selectionSort(nums):
    """选择排序法"""
    for i in range(len(nums) - 1):
        min_index = i
        # i位置默认最小值
        for j in range(i + 1, len(nums)):
            # 从 i+1 位置循环到末尾找最小值
            if nums[min_index] > nums[j]:
                # 如果出现小于i位置值，则交换
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


aList = [1, 9, 3, 7, 4, 5, 8, 2, 6]
print("selection_sort: %s" % selectionSort(aList))
