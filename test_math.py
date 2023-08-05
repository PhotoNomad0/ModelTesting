def filter_empty_strings(strings):
    return list(filter(None, strings))

strings = ["", "abc", "", "def", "ghi", ""]
print(filter_empty_strings(strings))
    
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

# from sympy.solvers import solve
# from sympy import Symbol
# 
# x = Symbol('x') # Define symbol for x
# a, b, c, d = 1, 0, 1, -130
# eq = a*x**3 + b*x**2 + c*x + d
# 
# sol = solve(eq)
# print("Correct Answer", sol)

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
