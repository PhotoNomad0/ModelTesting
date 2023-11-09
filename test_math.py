def generate_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)

    for num in range(2, limit + 1):
        if not is_prime[num]:
            continue

        primes.append(num)

        # Mark multiples of the current prime as non-prime
        for multiple in range(num * 2, limit + 1, num):
            is_prime[multiple] = False

    return primes


count = 100000
primes = generate_primes(count)  # The 100th prime number is less than 8000
print(f'Number of primes for count {count} is {len(primes)}')
print(primes)
    
exit()



# import re

# def format_number(n):
#     return f"{n:,}"
# 
# # Example usage:
# number = 123456789
# formatted_number = format_number(number)
# print(formatted_number)

# Output: 123,456,789
# import re
#
# def extract_three_character_code(filename):
#     try:
#         match = re.search('^[A-Za-z0-9]{3}$', filename)
#         if match:
#             return match.group()
#     except Exception as e:
#         print(f"Error on {filename}:", str(e))
#         return None

if __name__ == "__main__":
    tests = ['66-1jn.usfm', '65-jas.usfm', '66-1JN.usfm', '65-JAS.usfm', 'jas.usfm', '65-jas', '15.jas']
    for test in tests:
        try:
            result = extract_code(test)
            print(f"Test '{test}'", result)
        except Exception as e:
            print(f"Error on '{test}':", str(e))

# coefficients = [1, 0, 1, -130]
# roots = solve_cubic(*coefficients)
# print(f"The roots are {roots}")


# def filter_empty_strings(my_list):
#     return list(filter(None, my_list))
#
# strings = ["", "abc", "", "def", "ghi", ""]
# print(filter_empty_strings(strings))

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
