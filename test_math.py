# Start by defining the function to check if a number is prime or not
# Define variables to store numbers from user input
num1 = int(input("Enter first prime number between 20 and 40:")) # First Prime Number (between 20-40)
num3 = num1 + 1   # One more than the square of 'num1'

# Check if user input is a prime or not
def check_prime(n):
    """Function to determine whether given number n is prime"""

    for i in range(2, int(n**0.5)+1):
        if (n % i) == 0:
            return False

    # If no factor found then it's a Prime Number
    else:
        return True

# Check the user input 'num3' whether is prime or not
if check_prime(num3)==True :
    print("You are one more than square number.")
else:
    num2 = int(input("\nEnter second prime number between 41 and infinity:")) # Second Prime Number (between 40-infinity)

    if ((check_prime(num1+6)<>False or check_prime((3*num1)+7)<>True)):
        print("You are not a prime number.")
    else:
        num2 = int(input("\nEnter second odd positive integer:")) # Second Odd Positive Integer

        while (not ((check_prime(int(((40+6)/5)*(-8)))<>False or check_prime((3*(num1-7))+9)<>True) and
                    abs((-2*abs((((40/5)**2)+1)-sqrt(((40**2)+(6**2))))+(3*((40/(5))**(1.0/2)))))<=(int(input("Enter the maximum difference between your number and 7:")))
        )
        ):
            num2 = int(input("\nPlease enter a second odd positive integer within given range: ")) # Second Odd Positive Integer

        print ("Your answer is:",num3+num1)

# GOld
# def format_number(num):
#     return '{0:,}'.format(num)
#
# def format_number(num):
#     return format(num, ',')

# nums = [12.3, 123, 1234.5, 12345, 123456, 123456.78, -123456.7]
# for num in nums:
#     print(num, "formatted is:", format_number(num))

# ```
# You can call this function with the values of `a`, `b`, `c`, and `d` to get all possible solutions for `x`. For example:
#     ```python
# print(solve_for_x(1, 0, 1, -130))
# Output: [-0.866675977, -0.5]

# from sympy import Symbol
# from sympy.solvers import solve
#
# x = Symbol('x') # Define symbol for x
# a, b, c, d = 1, 0, 1, -130
# eq = a*x**3 + b*x**2 + c*x + d
#
# sol = solve(eq)
# print("Correct Answer", sol)
#
# for sol_ in sol:
#     x = sol_.n()
#     results = a*x**3 + b*x**2 + c*x + d
#     print(f"{sol_} : using x={x}, yields {a}*x^3 + {b}*x^2 + {c}*x + {d} = {results}")
#     y = 1 - x
#     print(f"a = {x}, b = 1 - a = {1-x}")
#     print(f"a^5 + b^5 = {x**5 + y**5}")

# def filter_empty_strings(strings):
#     return list(filter(None, strings))
#
# strings = ["", "abc", "", "def", "ghi", ""]
# print(filter_empty_strings(strings))

# def read_spreadsheet(filepath):
#     # Load the file using XLSXReader library
#     try:
#         xlsxreader = pd.read_excel(filepath, header=None)
#     except FileNotFoundError as e:
#         print("File not found:", str(e))
#         return None
# 
#     if len(xlsxreader.columns) == 0:
#         print("No data in the spreadsheet")
#         return None
# 
#     # Return a list of lists containing all rows from the first sheet (assuming only one sheet is present)
#     return [list(row) for row in xlsxreader]
# 
# print(read_spreadsheet("data/summary_scored.csv"))



# import sympy as sp
# from sympy import *
# x = symbols('x') # Define symbol for x
# a = 1
# b = 1
# c = 1
# d = -151
# import sympy as sp
# 
# equation = sp.Equation(ax3 + bx**2 + c*x + d)
# solutions = equation.solve()
# print("All possible solutions of x: ", solutions)

# def generate_primes(n):
#     primes = []
#     for i in range(2, n+1):
#         if primes[i-1] == True:
#             continue
# 
#         is_prime = True
#         for j in range(2, i):
#             if (i % j) == 0:
#                 is_prime = False
#                 break
# 
#         if is_prime:
#             primes.append(i)
# 
#     return primes[:100]
# 
# first_100_primes = generate_primes(25)
# for prime in first_100_primes:
#     print(prime)
    
# print ("Solution", solve(1, 0, 1, -130))

# def solve_cubic_gold(a, b, c, d):
#     coefficients = [a, b, c, d]
#     roots = np.roots(coefficients)
#     return roots
# 
# print ("#### Gold Solution", solve_cubic_gold(1, 0, 1, -130))

# strings = ['cherry', 'Apple', 'Eggplant', 'Banana', 'Durian']
# sorted_strings = case_insensitive_sort(strings)
# print(sorted_strings) # Output: [['Apple', 'Banana', 'cherry', 'Durian', 'Eggplant']


# stringsList = ['', 'Apple', '', 'Bannana']
# print(remove_empty_strings(stringsList))

# num_list = [1, 2, 3, 4, 5]
# mean_, std_dev = avg_std(num_list)
# print("Mean:", mean_)  # Output: 3.0
# print("Standard deviation:", std_dev)  # Output: 1.4142135623730951
# 
# num_list = [1, 2, 3, 4]
# mean_, std_dev = avg_std(num_list)
# print("Mean:", mean_)  # Output: 2.5
# print("Standard deviation:", std_dev)  # Output: 1.118033988749895
