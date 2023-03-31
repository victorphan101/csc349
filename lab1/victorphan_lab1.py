# This is a sample Python script.
import sys


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 1. list is ordered
# 2. list has 2k+1 elements
# 3. k of the numbers in the list appear twice
# 4. 1 is unique
# Divide and conquer
def singleton(numList, minIndex, maxIndex):
    # check if index error
    # check if max happens to be less than min, or there happens to check only two elements
    if maxIndex < minIndex or maxIndex-minIndex == 2:
        return -1

    # check if 1st element is singleton and check if only 1 element
    if len(numList[minIndex:maxIndex]) == 1 or numList[0] != numList[1]:
        return numList[minIndex]
    # check if last element
    if numList[len(numList)-2] != numList[len(numList)-1]:
        return numList[len(numList)-1]

    middle = int((maxIndex + minIndex) / 2)
    if maxIndex == minIndex:
        return numList[middle]

    # print(numList[middle])
    # print(len(numList[minIndex:maxIndex]))
    # print(numList[minIndex:maxIndex])

    if (maxIndex - minIndex) % 2 == 1:
        if (maxIndex - minIndex) % 4 == 1:
            if numList[middle - 1] == numList[middle]:
                return singleton(numList, minIndex, middle)
            elif numList[middle] == numList[middle + 1]:
                return singleton(numList, middle, maxIndex)
            else:
                return numList[middle]
        elif (maxIndex - minIndex) % 4 == 3:
            if numList[middle - 1] == numList[middle]:
                return singleton(numList, middle + 1, maxIndex)
            elif numList[middle] == numList[middle + 1]:
                return singleton(numList, minIndex, middle)
            return numList[middle]
    else:
        if numList[middle - 1] == numList[middle]:
            return singleton(numList, minIndex, middle+1)
        elif numList[middle] == numList[middle + 1]:
            return singleton(numList, middle, maxIndex)
        return numList[middle]


def main():
    # read file
    args = sys.argv[1:]
    file = open(args[0], 'r')
    numList = []
    for num in file:
        numList.append(int(num.strip()))
    file.close()
    print(singleton(numList, 0, len(numList)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
