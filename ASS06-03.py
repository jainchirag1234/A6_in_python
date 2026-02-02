"""
Q.3. Write a Python program to do the following: 
 Define a class myDate consisting of attributes day, month and year and following 
methods: 
o addDays(myDate, int) where the 1st argument is a myDate class type and 2nd 
argument is an integer type with default value as 0. The method should 
add/subtract int days (depending on the integer i.e. add if positive and 
subtract if negative) to/from the myDate and return new date of myDate type. 
o formatDate(myDate, formatString) where the 1st argument is a myDate class 
type and 2nd argument is a format string of string type. The method will return 
the date in the given format. Consider only the following format strings in 
this program. ‘dd-mm-yyyy’, ‘mm-dd-yyyy’ and ‘yyyy-mm-dd’. 
 Implement the above 
"""

from datetime import date, timedelta

class myDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def addDays(self, days=0):
        """
        Adds (or subtracts, if days is negative) a given number of days to/from the current date.
        Returns a new myDate object with the updated date.
        """
        # Convert the current myDate to a datetime.date object.
        current_date = date(self.year, self.month, self.day)
        # Add/subtract days using timedelta.
        new_date = current_date + timedelta(days=days)
        # Return a new myDate instance with the updated values.
        return myDate(new_date.day, new_date.month, new_date.year)

    def formatDate(self, formatString):
        """
        Returns the date as a string formatted according to the given formatString.
        Supported formats:
          - 'dd-mm-yyyy'
          - 'mm-dd-yyyy'
          - 'yyyy-mm-dd'
        If the format is not recognized, defaults to 'dd-mm-yyyy'.
        """
        if formatString == "dd-mm-yyyy":
            return f"{self.day:02d}-{self.month:02d}-{self.year:04d}"
        elif formatString == "mm-dd-yyyy":
            return f"{self.month:02d}-{self.day:02d}-{self.year:04d}"
        elif formatString == "yyyy-mm-dd":
            return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"
        else:
            return f"{self.day:02d}-{self.month:02d}-{self.year:04d}"

    def __str__(self):
        # This will help display the date in a default format.
        return self.formatDate("dd-mm-yyyy")


# Main script to test and validate the myDate class functionality.
if __name__ == "__main__":
    # Create a myDate object for August 15, 2023.
    original_date = myDate(15, 8, 2023)
    print("Original Date:", original_date.formatDate("dd-mm-yyyy"))
    
    # Add 10 days to the original date.
    new_date = original_date.addDays(10)
    print("After Adding 10 Days:", new_date.formatDate("dd-mm-yyyy"))
    
    # Subtract 20 days from the original date.
    earlier_date = original_date.addDays(-20)
    print("After Subtracting 20 Days:", earlier_date.formatDate("dd-mm-yyyy"))
    
    # Display the original date in different formats.
    print("Date in 'mm-dd-yyyy' format:", original_date.formatDate("mm-dd-yyyy"))
    print("Date in 'yyyy-mm-dd' format:", original_date.formatDate("yyyy-mm-dd"))
