def sorted_case_insensitive(strings):
    return sorted([x.lower() for x in strings])

# Example usage
strings = ['cherry', 'Apple', 'Banana', 'eggplant', 'Durian']
sorted_strings = sorted_case_insensitive(strings)
print(sorted_strings) # Output: ['apple', 'banana', 'Cherry', 'durian', 'eggplant']