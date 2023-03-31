# This is a sample Python script.
import sys


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def edit_distance(nString, mString):
    # base case: n or m empty
    # Given n and m strings
    n = len(nString)
    m = len(mString)

    # Populate n by m matrix
    E = [[0] * (n+1) for _ in range(m+1)]

    for nVal in range(n+1):
        E[0][nVal] = nVal
    for mVal in range(m+1):
        E[mVal][0] = mVal

    for mVal in range(1, m+1):
        for nVal in range(1, n+1):
            if nString[nVal-1] == mString[mVal-1]:
                E[mVal][nVal] = E[mVal-1][nVal-1]
            else:
                E[mVal][nVal] = 1 + min(E[mVal-1][nVal], E[mVal][nVal-1], E[mVal-1][nVal-1])

    return E[-1][-1]


def main():
    n_string = sys.argv[1]
    m_string = sys.argv[2]

    print(edit_distance(n_string, m_string))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
