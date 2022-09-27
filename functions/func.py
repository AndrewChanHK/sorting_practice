import random

from models.enum import *
from utils.bubble_sort import *
from utils.selection_sort import *


def getRandomNums() -> list:
    # Generate 15 random nums
    nums = random.sample(range(100), 15)
    if isSorted(nums):
        getRandomNums()
    return nums


def sorting(nums: list, type: SortType) -> list:
    # Apply related sorting
    match type:
        case SortType.bubbleSort: return bubbleSort(nums)
        case SortType.selectionSort: return selectionSort(nums)
        case SortType.insertionSort: pass
        case SortType.mergeSort: pass
        case SortType.quickSort: pass


def isSorted(nums: list) -> bool:
    return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
