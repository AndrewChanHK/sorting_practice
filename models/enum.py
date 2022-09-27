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
            case SortType.bubbleSort: return 'Bubble Sort'
            case SortType.selectionSort: return 'Selection Sort'
            case SortType.insertionSort: return 'Insertion Sort'
            case SortType.mergeSort: return 'Merge Sort'
            case SortType.quickSort: return 'Quick Sort'

    def getSortType(val: int):
        # Return related type
        for e in SortType:
            if e.value == val:
                return e

    def printAllType():
        for e in SortType:
            print('- ', e.value, e.getName())
