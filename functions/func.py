import random

from controllers.sorting_controller import SortingController


def getRandomNums() -> list:
    # Generate 15 random nums
    nums = random.sample(range(100), 15)
    if SortingController().isSorted(nums):
        getRandomNums()
    return nums
