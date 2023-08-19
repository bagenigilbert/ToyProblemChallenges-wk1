## Gilbert Bagen's Awesome Time Converter
Hey there! Welcome to the Gilbert Bagen's Awesome Time Converter repository. In this simple guide, we'll show you how to use Gilbert Bagen's clever functions to convert time from the regular 12-hour format to the cool 24-hour format, count positive numbers like a pro, and calculate the value of consonant-packed words.

## Functions
# 1. Convert 12-Hour Time to 24-Hour Time
Function: convert_to_24_hours(hour, minute, period)

This nifty function takes your time in the morning or evening and transforms it into the modern 24-hour format. Let's see it in action:
# Convert 8:30 AM to 24-hour format
print(convert_to_24_hours(8, 30, "AM"))  # Output: "08:30"

# Convert 8:30 PM to 24-hour format
print(convert_to_24_hours(8, 30, "PM"))  # Output: "20:30"
# 2. Count Exactly Two Positive Numbers
# Function: exactly_two_positive(a, b, c)

This magical function tells you whether you've got exactly two positive numbers out of three. It's like counting your marbles, but with numbers! Check it out:

# Check if exactly two out of three numbers are positive
print(exactly_two_positive(2, 4, -3))  # Output: True
print(exactly_two_positive(-4, 6, 8))  # Output: True
print(exactly_two_positive(4, -6, 9))  # Output: True
print(exactly_two_positive(-4, 6, 0))  # Output: False
# 3. Calculate Consonant Value
Function: consonant_value(s)

Ever wondered how much consonant power a word holds? This function calculates the value of consonant-packed words and gives you a taste of their awesomeness:
# Calculate the value of consonants in a word
print(consonant_value("zodiacs"))  # Output: 26
print(consonant_value("strength"))  # Output: 57
# How to Use
Make sure you've got Python installed on your computer.
Download or clone this repository.
Open your terminal and navigate to the repository's directory.
Use the functions in your own code by importing them. For example:

## from gilbert_bagen_utils import convert_to_24_hours

# Now you can use convert_to_24_hours function as shown earlier!
## Author
This amazing code was created by Gilbert Bagen. If you have any questions, suggestions, or just want to say hi, feel free to reach out to Gilbert at gilbertwilber0@gmail.com.

That's it! Have fun converting time, counting numbers, and discovering the power of consonants with Gilbert Bagen's incredible functions. Happy coding!