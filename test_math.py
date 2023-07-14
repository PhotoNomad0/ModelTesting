import math

numbers = [1, 2, 3, 4] # replace this line with your own list of numbers
total_sum = sum(numbers) # calculate the total sum of all the numbers in the list
average = total_sum / len(numbers) # divide the total by the number of items to get the average
variance = sum((x - average) ** 2 for x in numbers) // (len(numbers)) # calculate the variance using the formula
std_dev = math.sqrt(variance) # take the square root of the variance to get the standard deviation
print("The average is:", average)
print("The standard deviation is:", std_dev)

# num_list = [1, 2, 3, 4, 5]
# mean_, std_dev = avg_std(num_list)
# print("Mean:", mean_)  # Output: 3.0
# print("Standard deviation:", std_dev) # Output: 1.4142135623730951
# 
# num_list = [1, 2, 3, 4]
# mean_, std_dev = avg_std(num_list)
# print("Mean:", mean_)  # Output: 3.0
# print("Standard deviation:", std_dev) 