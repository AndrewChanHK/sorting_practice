def selectionSort(nums: list) -> list:
    for swapKey in range(len(nums)-1):
        minKey = swapKey
        for i in range(swapKey+1, len(nums)):
            if nums[i] < nums[minKey]:
                minKey = i
        nums[swapKey], nums[minKey] = nums[minKey], nums[swapKey]
    return nums
