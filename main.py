import random
from ast import match_case
from enum import Enum, auto
from tokenize import Double
from utils.bubble_sort import bubbleSort


class SortType(Enum):
    bubbleSort = auto()
    selectionSort = auto()
    insertionSort = auto()
    mergeSort = auto()
    quickSort = auto()
    # etc

    def printAll():
        for e in SortType:
            print(e.value, e.name)


def getRandomNums() -> list:
    # Generate 15 random nums
    return random.sample(range(100), 15)


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
        case SortType.selectionSort: pass
        case SortType.insertionSort: pass
        case SortType.mergeSort: pass
        case SortType.quickSort: pass


def main():
    nums = getRandomNums()
    print('Unsorted numbers: ', nums)

    SortType.printAll()
    val = input('Choose the sorting:')
    sortType = getSortType(int(val))
    print('Sorting by using %s... ' % sortType.name)

    res = sorting(nums, sortType)

    print('Sorted numbers: ', res)


main()
