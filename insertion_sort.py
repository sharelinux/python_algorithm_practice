def insertionSort01(nums):
    """插入排序法"""
    for i in range(len(nums)):
        current_value = nums[i]
        position = i

        while position > 0 and nums[position - 1] > current_value:
            nums[position] = nums[position - 1]
            position -= 1

        nums[position] = current_value

    return nums


aList = [1, 9, 3, 7, 4, 5, 8, 2, 6]
print("insertion_sort01: %s" % insertionSort01(aList))


def insertionSort02(nums):
    """插入排序法"""
    for i in range(len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]

    return nums


aList = [1, 9, 3, 7, 4, 5, 8, 2, 6]
print("insertion_sort02: %s" % insertionSort02(aList))
