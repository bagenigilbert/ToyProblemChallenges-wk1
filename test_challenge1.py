import challenge1

def test_convert_am():
    assert challenge1.convert_to_24_hours(8, 30, "AM") == "08:30"

def test_convert_pm():
    assert challenge1.convert_to_24_hours(8, 30, "PM") == "20:30"

def test_midnight_am():
    assert challenge1.convert_to_24_hours(12, 0, "AM") == "00:00"

def test_midnight_pm():
    assert challenge1.convert_to_24_hours(12, 0, "PM") == "12:00"

def test_noon_am():
    assert challenge1.convert_to_24_hours(12, 0, "AM") == "00:00"

def test_noon_pm():
    assert challenge1.convert_to_24_hours(12, 0, "PM") == "12:00"

def test_hour_edge_case():
    assert challenge1.convert_to_24_hours(1, 0, "AM") == "01:00"
    assert challenge1.convert_to_24_hours(11, 0, "AM") == "11:00"
    assert challenge1.convert_to_24_hours(1, 0, "PM") == "13:00"
    assert challenge1.convert_to_24_hours(11, 0, "PM") == "23:00"

# Run the testsa
test_convert_am()
test_convert_pm()
test_midnight_am()
test_midnight_pm()
test_noon_am()
test_noon_pm()
test_hour_edge_case()

print("All tests passed!")
