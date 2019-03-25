"""
    Task
    Given an integer, , perform the following conditional actions:

    If n is odd, print Weird
    If n is even and in the inclusive range of 2 to 5, print Not Weird
    If n is even and in the inclusive range of 6 to 20, print Weird
    If n is even and greater than 20, print Not Weird
"""
# !/bin/python3
n = int(input())

is_odd = n % 2

# If  is even and in the inclusive range of  to , print Not Weird
if 2 <= n <= 5 and not is_odd:
    print("Not Weird")
elif 6 <= n <= 20 and not is_odd:
    print("Weird")
elif n > 20 and not is_odd:
    print("Not Weird")
elif is_odd:
    print("Weird")


