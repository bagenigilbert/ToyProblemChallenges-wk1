# Define a function to check if exactly two out of three numbers are positive
def exactly_two_positive(a, b, c):
    # Initialize a variable to keep track of the count of positive numbers
    count_positive = 0
    
    # Check if each number is positive, and if so, increment the count
    if a > 0:
        count_positive += 1
    if b > 0:
        count_positive += 1
    if c > 0:
        count_positive += 1
    
    # Check if the count of positive numbers is equal to 2
    return count_positive == 2

# Test cases
# Call the function with different inputs and print the results
print(exactly_two_positive(2, 4, -3))  # Output: True
print(exactly_two_positive(-4, 6, 8))  # Output: True
print(exactly_two_positive(4, -6, 9))  # Output: True
print(exactly_two_positive(-4, 6, 0))  # Output: False
