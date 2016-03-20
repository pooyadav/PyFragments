# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the 
# non-negative numbers. The runtime of your program should be 
# proportional to the LOGARITHM of the input. You may want to 
# do some research into binary search and Newton's method to 
# help you out.
#
# This function should return another function which computes the
# inverse of the input function. 
#
# Your inverse function should also take an optional parameter, 
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The 
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is 
# efficient enough. 

def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1 

# Actually I think my solution is better than PN's this time
def inverse(f, delta = 1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(b):
        x = 0; alpha = delta
        while f(x) < b:
            alpha *= 2 
            x += alpha
        return bisearch(f, b, x - alpha, x)
    return f_1

def close_enough(a, b) : 
    tolerance = .0001
    return abs(a - b) < tolerance

def bisearch(f,neg, pos, b=0):
    mid = (neg + pos)/2.
    if close_enough(neg, pos) : return mid
    test_value = f(mid)
    if test_value > b :
        return bisearch(f, b, neg, mid)
    elif test_value < b:
        return bisearch(f, b, mid, pos)
    else:
        return mid

## Code from SICP, but no use here
## I was too obssessed with using newton method.
#def deriv(g):
#    dx = 0.0001
#    return lambda x : (g(x + dx) - g(x)) * 1. / dx
#def newton_transform(g):
#    return lambda x : x - g(x) * 1. / deriv(g)(x)
#def newton_method(g, guess):
#    return fixed_point(newton_transform(g), guess)
#def fixed_point(f, first_guess):
#    tolerance = 0.00001
#    def close_enough(a, b) : return abs(a - b) < tolerance
#    def tryx(guess):
#        nextx = f(guess)
#        return nextx if close_enough(guess, nextx) else tryx(nextx)
#    return tryx(first_guess)
    
def square(x): return x*x
sqrt = slow_inverse(square)

print sqrt(1000000000)
