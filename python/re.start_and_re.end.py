"""
https://www.hackerrank.com/challenges/re-start-re-end/problem
"""
import re


def match(s: str, k: str) -> None:
    exist = False
    for i in range(len(s)):
        j = 0
        if s[i] != k[j]:
            continue
        
        tmp_i = i
        
        while tmp_i < len(s) and j < len(k) and s[tmp_i] == k[j]:
            tmp_i += 1
            j += 1
        
        if s[i:tmp_i] == k:
            exist = True
            print((i, tmp_i - 1))

    if not exist:
        print((-1, -1))


def match2(s: str, k: str) -> None:
    pattern = re.compile(k)
    m = pattern.search(s)
    if not m:
        print((-1, -1))
        return
    while m:
        start, end = m.start(), m.end() - 1
        print((start, end))
        m = pattern.search(s, pos=start + 1)

        
def main() -> None:
    s: str = input()
    k: str = input()
    match(s, k)


if __name__ == "__main__":
    main()
