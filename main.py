import random
from ast import match_case
from enum import Enum, auto
from tokenize import Double


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
    return random.sample(range(20), 15)


def getSortType(val: int) -> SortType:
    # Return related type
    for e in SortType:
        if e.value == val:
            return e


def sorting(type: SortType):
    # Apply related sorting
    match type:
        case SortType.bubbleSort: pass
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

    sorting(sortType)


main()
