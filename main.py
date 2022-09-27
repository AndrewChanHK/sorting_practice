import random
from ast import match_case
from enum import Enum, auto
from tokenize import Double
from utils.bubble_sort import bubbleSort
from utils.selection_sort import selectionSort


class SortType(Enum):
    bubbleSort = auto()
    selectionSort = auto()
    insertionSort = auto()
    mergeSort = auto()
    quickSort = auto()
    # etc

    def printAll():
        for e in SortType:
            print('- ', e.value, e.name)


def getRandomNums() -> list:
    # Generate 15 random nums
    nums = random.sample(range(100), 15)
    if isSorted(nums):
        getRandomNums()
    return nums


def getSortType(val: int) -> SortType:
    # Return related type
    for e in SortType:
        if e.value == val:
            return e


def sorting(nums: list, type: SortType) -> list:
    # Apply related sorting
    match type:
        case SortType.bubbleSort:
            return bubbleSort(nums)
        case SortType.selectionSort:
            return selectionSort(nums)
        case SortType.insertionSort: pass
        case SortType.mergeSort: pass
        case SortType.quickSort: pass


def isSorted(nums: list) -> bool:
    return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))


def main():
    nums = getRandomNums()
    print('Unsorted numbers: ', nums)

    SortType.printAll()
    val = input('Choose the sorting:')
    sortType = getSortType(int(val))
    print('Sorting by using %s... ' % sortType.name)

    res = sorting(nums, sortType)

    if isSorted(nums):
        print('Sorted numbers: ', res)
    else:
        print('---Error found---')


if __name__ == '__main__':
    main()
