from functions.func import getRandomNums, isSorted, sorting
from models.enum import SortType


def main():
    nums = getRandomNums()
    print('Unsorted numbers: ', nums)

    SortType.printAllType()
    val = input('Choose the sorting:')
    sortType = SortType.getSortType(int(val))
    print('Sorting by using %s... ' % sortType.getName())

    res = sorting(nums, sortType)

    if isSorted(nums):
        print('Sorted numbers: ', res)
    else:
        print('---Error found---')


if __name__ == '__main__':
    main()
