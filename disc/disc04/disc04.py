from ucb import trace

#1.1
def count_stair_ways(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        next_one_steps = count_stair_ways(n-1)
        next_two_steps = count_stair_ways(n-2)
        return next_one_steps + next_two_steps
 
def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n < 0 or k == 0:
        return 0
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n-i, k)
            i += 1
        return total
    
#2.1
1, 3

5

False

True

2

#2.2
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i * s[i] for i in range(len(s)) if i % 2 == 0]

#2.3
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s==[]:
        return 1
    else:
        max_value = 1
        for i in range(len(s)):
            temp_value = s[i] * max_product(s[i+2:])
            max_value = temp_value if temp_value >= max_value else max_value
        return max_value

