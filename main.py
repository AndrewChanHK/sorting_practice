from controllers.sorting_controller import SortingController
from functions.func import getRandomNums
from models.enum import SortType


def main():
    nums = getRandomNums()
    print('Unsorted numbers: ', nums)

    SortType.printAllType()
    val = input('Choose the sorting:')
    sortType = SortType.getSortType(int(val))
    print('Sorting by using %s... ' % sortType.getName())

    controller = SortingController()

    res = controller.sort(nums, sortType)

    if controller.isSorted(nums):
        print('Sorted numbers: ', res)
    else:
        print('---Error found---')


if __name__ == '__main__':
    main()
