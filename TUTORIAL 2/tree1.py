def factorial(n):
   if n == 0: # Base case
       return 1
   else:
       return n * factorial(n - 1)

print(factorial(5)) # Output: 120
