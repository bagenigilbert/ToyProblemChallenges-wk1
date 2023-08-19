# Define a function to convert 12-hour time to 24-hour time
def convert_to_24_hours(hour, minute, period):
    # Check if the given period is "am"
    if period == 'AM':
        # If it's midnight (12 am), set the hour to 0
        if hour == 12:
            hour = 0
    else: 
         # If it's not "am" (i.e., it's "pm")
        # and the hour is not noon (12 pm), add 12 to the hour        
        if hour != 12:
            hour += 12
            
    # Use f-string formatting to format the hour and minute as two-digit strings
    # The :02d inside the curly braces ensures that each number is at least two digits
    # and is padded with leading zeros if needed
    # Finally, concatenate the formatted hour and minute to create the 24-hour time
    return f"{hour:02d}:{minute:02d}"

# Test cases
# Call the function with different inputs and print the results
print(convert_to_24_hours(8, 30, "AM"))
print(convert_to_24_hours(8, 30, "PM"))
