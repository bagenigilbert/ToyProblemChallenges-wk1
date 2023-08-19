# Define a function that calculates the value of consonant substrings in a string
def consonant_value(s):
    # Define a string containing all consonant characters
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    # Initialize variables to keep track of the maximum value and current value
    max_value = 0
    current_value = 0
    
    # Iterate through each character in the input string 's'
    for char in s:
        if char in consonants:  # Check if the character is a consonant
            # Calculate the value of the consonant using ASCII values
            current_value += ord(char) - ord("a") + 1
        else:
            # If the character is not a consonant, update the maximum value
            # and reset the current value to 0
            max_value = max(max_value, current_value)
            current_value = 0
    
    # Return the maximum value of consonant substrings
    return max(max_value, current_value)

# Test cases and expected outputs
print(consonant_value("zodiacs"))  # Expected output: 26
print(consonant_value("strength"))  # Expected output: 57
