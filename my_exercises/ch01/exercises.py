# R-1.1

def is_multiple(n,m):
    if n % m == 0:
        return True
    return False
print(is_multiple(15,5))


# R-1.2 - cannot use multiplication, divison operators or modulo

def is_even(k):
    n = abs(k)
    if int(bin(n)[-1:]) == 0:
        return True
    return False

print(is_even(1))
print(is_even(4))
print(is_even(11))
print(is_even(-355))
print(is_even(-1))
print(is_even(0))
print(is_even(4661))


# R-1.3 - donotuse minmax funcs

def minmax(data):
    s = data[0]
    l = 0
    for d in data:
        if d < s:
            s = d
        if d > l:
            l = d
        else:
            pass
    return s,l

print(minmax([2,3,4,5,6,7,8,9]))


# R-1.4 - sum of squares of numbers less than n (n is positive)

def sum_positive_squares(n):
    squares =[]
    for x in range(1,n):
        squares.append(x*x)
    return sum(squares)

print(sum_positive_squares(6))


# R-1.5 - same as above but with python comprenhension

def sum_positive_squares_comp(n):
    return sum([x*x for x in range(1,n)])

print(sum_positive_squares_comp(6))