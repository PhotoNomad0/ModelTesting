import numpy as np
import math

def solve_for_x(a, b, c, d):
    # check if the discriminant is negative 
    if (b**2 - 4*a*c) < 0:
        print("No real solutions")
    else:
        # get the square root of the discriminant 
        sqrtd = ((-b + sqrt(discr))/(2 * a))

        if (sqrtd == int(sqrtd)):
            print("x = ", int(sqrtd))
        else:
            # get the other root 
            other_root = (-b - sqrt(discr))/(2 * a)

            if (other_root == int(other_root)):
                print("x = ", int(other_root))
            else:
                # check for complex numbers 
                if ((sqrtd + other_root).imag != 0):
                    print("No real solutions")
                else:
                    print("x = ", sqrtd)
                    
# Driver code to test the above function 
a = 1
b = 0
c = 1
d = -130
solve_for_x(a, b, c, d)


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
