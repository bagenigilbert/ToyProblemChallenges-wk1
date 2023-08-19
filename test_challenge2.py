import challenge2  # Import your main code file

# Test cases for exactly_two_positive function
def test_positive_case():
    assert challenge2.exactly_two_positive(2, 4, -3) == True

def test_all_positive_case():
    assert challenge2.exactly_two_positive(2, 6, 8) == False

def test_two_positive_case():
    assert challenge2.exactly_two_positive(4, -6, 9) == True

def test_no_positive_case():
    assert challenge2.exactly_two_positive(-4, -6, 0) == False

# Run the tests
test_positive_case()
test_all_positive_case()
test_two_positive_case()
test_no_positive_case()

print("All tests passed!")
