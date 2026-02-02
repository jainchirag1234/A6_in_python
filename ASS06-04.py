"""
Q.4. Write a Python program to overload: 
 the ‘+’ operator for the string as under: 
The 2 strings should be merged in such a way that the result will contain characters 
one by one first from the 1st string and then from the 2nd string as shown in the 
example given below.  
Str1=’VNSGU’ 
Str2=’SURAT’ 
Then Str1+Str2 = ‘VSNUSRGAUT’ (i.e. here characters in Italics are from Str1 and 
rest from Str2) 
 the <, <=, >, >= and == operators for the strings as under: 
Compare sum of ACII values of all the characters in both the strings and then 
compare the results. Return True if the sum for the 1st string is more than that for the 
2nd string for the ‘>’ operator and False otherwise. Similarly do for other operators.
"""

class CustomString:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        """
        Overloads the '+' operator to merge two strings such that characters
        alternate from self and other. If the strings are of unequal length,
        the remaining characters of the longer string are appended at the end.
        """
        merged = ""
        min_len = min(len(self.value), len(other.value))
        # Alternate characters from both strings.
        for i in range(min_len):
            merged += self.value[i] + other.value[i]
        # Append any remaining characters from the longer string.
        if len(self.value) > min_len:
            merged += self.value[min_len:]
        if len(other.value) > min_len:
            merged += other.value[min_len:]
        return CustomString(merged)

    def ascii_sum(self):
        """
        Computes the sum of the ASCII values of all characters in the string.
        """
        return sum(ord(ch) for ch in self.value)

    def __gt__(self, other):
        """Overloads '>' operator based on ASCII sum comparison."""
        return self.ascii_sum() > other.ascii_sum()

    def __lt__(self, other):
        """Overloads '<' operator based on ASCII sum comparison."""
        return self.ascii_sum() < other.ascii_sum()

    def __ge__(self, other):
        """Overloads '>=' operator based on ASCII sum comparison."""
        return self.ascii_sum() >= other.ascii_sum()

    def __le__(self, other):
        """Overloads '<=' operator based on ASCII sum comparison."""
        return self.ascii_sum() <= other.ascii_sum()

    def __eq__(self, other):
        """Overloads '==' operator based on ASCII sum comparison."""
        return self.ascii_sum() == other.ascii_sum()

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"CustomString('{self.value}')"


# Main program to demonstrate the overloaded operators
if __name__ == "__main__":
    # Create two CustomString objects.
    s1 = CustomString("VNSGU")
    s2 = CustomString("SURAT")
    
    # Demonstrate the overloaded '+' operator.
    merged = s1 + s2
    print("Merged string (s1 + s2):", merged)  # Expected: "VSNUSRGAUT"
    
    # Calculate and display the ASCII sum for both strings.
    print("ASCII Sum of s1:", s1.ascii_sum())
    print("ASCII Sum of s2:", s2.ascii_sum())
    
    # Demonstrate the overloaded comparison operators.
    print("s1 > s2:", s1 > s2)
    print("s1 < s2:", s1 < s2)
    print("s1 == s2:", s1 == s2)
    print("s1 >= s2:", s1 >= s2)
    print("s1 <= s2:", s1 <= s2)
