from models.enum import SortType
from utils.bubble_sort import bubbleSort
from utils.insertion_sort import insertionSort
from utils.selection_sort import selectionSort


class SortingController:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sort(self, nums: list, type: SortType) -> list:
        # Apply related sorting
        match type:
            case SortType.bubbleSort: return bubbleSort(nums)
            case SortType.selectionSort: return selectionSort(nums)
            case SortType.insertionSort: return insertionSort(nums)
            case SortType.mergeSort: pass
            case SortType.quickSort: pass

    def isSorted(self, nums: list) -> bool:
        return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
