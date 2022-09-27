def bubbleSort(nums: list) -> list:
    for i in range(len(nums) - 1):
        swapped = False
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums
