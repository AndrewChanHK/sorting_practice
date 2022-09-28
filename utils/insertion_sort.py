def insertionSort(nums: list) -> list:
    for i in range(1, len(nums)):
        insertKey = i-1
        minNum = nums[i]
        while insertKey >= 0 and nums[insertKey] > minNum:
            nums[insertKey+1] = nums[insertKey]
            insertKey -= 1
        nums[insertKey+1] = minNum
    return nums
