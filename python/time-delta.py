"""
https://www.hackerrank.com/challenges/python-time-delta/problem
"""

import os
import datetime


# Complete the time_delta function below.
def time_delta(t1, t2) -> str:
    # Sun 10 May 2015 13:54:36 -0700
    format_ = '%a %d %b %Y %H:%M:%S %z'
    d1 = datetime.datetime.strptime(t1, format_)
    d2 = datetime.datetime.strptime(t2, format_)
    return str(abs(int((d1 - d2).total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()
