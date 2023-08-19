# Import the main code file for testing
import challenge3

# Test cases for consonant_value function
def test_consonant_value_zodiacs():
    # Test with the input "zodiacs", the output should be 26
    assert challenge3.consonant_value("zodiacs") == 26

def test_consonant_value_strength():
    # Test with the input "strength", the output should be 57
    assert challenge3.consonant_value("strength") == 57

def test_consonant_value_empty_string():
    # Test with an empty string as input, the output should be 0
    assert challenge3.consonant_value("") == 0

def test_consonant_value_single_consonant():
    # Test with a single consonant "b" as input, the output should be 2
    assert challenge3.consonant_value("b") == 2

def test_consonant_value_single_vowel():
    # Test with a single vowel "e" as input, the output should be 0
    assert challenge3.consonant_value("e") == 0

def test_consonant_value_mixed_case():
    # Test with mixed case input "Happiness", the output should be 38
    assert challenge3.consonant_value("Happiness") == 38

# Run the tests
test_consonant_value_zodiacs()
test_consonant_value_strength()
test_consonant_value_empty_string()
test_consonant_value_single_consonant()
test_consonant_value_single_vowel()
test_consonant_value_mixed_case()

# Print a message indicating that all tests passed
print("All tests passed!")
