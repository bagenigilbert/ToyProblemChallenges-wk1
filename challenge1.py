# define  a function to convert 12-hour time to 24-hour time
def convert_to_24_hours(hour,time,period):
    #check if the given period is "am"
    if period == "AM":
        # If it's midnight (12 am), set the hour to 0

