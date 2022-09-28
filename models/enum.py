from enum import Enum, auto


class SortType(Enum):
    bubbleSort = auto()
    selectionSort = auto()
    insertionSort = auto()
    mergeSort = auto()
    quickSort = auto()
    # etc

    def getName(self) -> str:
        match self:
            case SortType.bubbleSort:  res = 'Bubble Sort'
            case SortType.selectionSort:  res = 'Selection Sort'
            case SortType.insertionSort:  res = 'Insertion Sort'
            case SortType.mergeSort:  res = 'Merge Sort'
            case SortType.quickSort:  res = 'Quick Sort'
        return res

    def getSortType(val: int):
        # Return related type
        for e in SortType:
            if e.value == val:
                return e

    def printAllType():
        for e in SortType:
            print('- ', e.value, e.getName())
