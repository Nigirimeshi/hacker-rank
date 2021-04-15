"""
https://www.hackerrank.com/challenges/python-lists/problem
"""

INSERT = "insert"
PRINT = "print"
REMOVE = "remove"
APPEND = "append"
SORT = "sort"
POP = "pop"
REVERSE = "reverse"


def main():
    arr: List[int] = []
    for _ in range(int(input())):
        args = input().split(' ')
        opt = args[0]
        if opt == INSERT:
            index, value = int(args[1]), int(args[2])
            arr.insert(index, value)
        elif opt == PRINT:
            print(arr)
        elif opt == REMOVE:
            value = int(args[1])
            if value in arr:
                arr.remove(value)
        elif opt == APPEND:
            value = int(args[1])
            arr.append(value)
        elif opt == SORT:
            arr.sort()
        elif opt == POP:
            arr.pop()
        elif opt == REVERSE:
            arr.reverse()


if __name__ == '__main__':
    main()