from models.enum import SortType
from utils.bubble_sort import bubbleSort
from utils.insertion_sort import insertionSort
from utils.merge_sort import mergeSorting
from utils.quick_sort import quickSort
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
            case SortType.bubbleSort: res = bubbleSort(nums)
            case SortType.selectionSort:  res = selectionSort(nums)
            case SortType.insertionSort:  res = insertionSort(nums)
            case SortType.mergeSort:  res = mergeSorting(nums)
            case SortType.quickSort:  res = quickSort(nums)
        return res

    def isSorted(self, nums: list) -> bool:
        return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
