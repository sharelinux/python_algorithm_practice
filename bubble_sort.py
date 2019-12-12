def bubbleSort(nums):
    """冒泡排序法"""
    for i in range(len(nums)-1):
        # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-i-1):
            # ｊ为列表下标
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums


aList = [1, 9, 3, 7, 4, 5, 8, 2, 6]
print("bubble_sort: %s" % bubbleSort(aList))
