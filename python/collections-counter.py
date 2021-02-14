"""
https://www.hackerrank.com/challenges/collections-counter/problem
"""
from collections import Counter


if __name__ == '__main__':
    x = int(input())
    shoe_sizes = list(map(int, input().split(' ')))
    n = int(input())
    customer_wanted_shoe_sizes_and_price = (
        list(map(int, input().split(' '))) for i in range(n)
    )
    
    amount = 0
    shoe_sizes_idx = Counter(shoe_sizes)
    for size, price in customer_wanted_shoe_sizes_and_price:
        if size in shoe_sizes_idx:
            amount += price
            shoe_sizes_idx[size] -= 1
            if shoe_sizes_idx[size] == 0:
                shoe_sizes_idx.pop(size)
    print(amount)
