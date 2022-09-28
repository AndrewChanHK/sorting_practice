def mergeSorting(nums: list) -> list:
    if len(nums) > 1:
        mid = len(nums)//2
        leftNums = nums[:mid]
        rightNums = nums[mid:]

        mergeSorting(leftNums)
        mergeSorting(rightNums)

        leftIdx = rightIdx = idx = 0

        while leftIdx < len(leftNums) and rightIdx < len(rightNums):
            if leftNums[leftIdx] < rightNums[rightIdx]:
                nums[idx] = leftNums[leftIdx]
                leftIdx += 1
                idx += 1
            else:
                nums[idx] = rightNums[rightIdx]
                rightIdx += 1
                idx += 1

        while leftIdx < len(leftNums):
            nums[idx] = leftNums[leftIdx]
            leftIdx += 1
            idx += 1

        while rightIdx < len(rightNums):
            nums[idx] = rightNums[rightIdx]
            rightIdx += 1
            idx += 1

    return nums
