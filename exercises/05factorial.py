# Write a function to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example function call
#
# factorial(5)
#
# > 120
#

def factorial(n):
  # start the running total
  total = 1
  # loop in the range up to n
  for i in range(1, n + 1):
    # multiply the total by the current number
    total *= i
    print(f'i is {i} total is {total}')

  return total 

solv = factorial(5)
print(solv)