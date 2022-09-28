
def partition(nums: list, low: int, high: int) -> int:
    piKey = high
    swapKey = low
    for i in range(low, high):
        if nums[i] < nums[piKey]:
            nums[swapKey], nums[i] = nums[i], nums[swapKey]
            swapKey += 1
    nums[swapKey], nums[piKey] = nums[piKey], nums[swapKey]
    return swapKey


def sort(nums: list, low: int, high: int):
    if low < high:
        pi = partition(nums, low, high)
        sort(nums, low, pi-1)
        sort(nums, pi+1, high)


def quickSort(nums: list) -> list:
    sort(nums, 0, len(nums)-1)
    return nums
