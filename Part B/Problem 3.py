# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def isPalindrome(str):
    if len(str)== 0 or len(str) == 1:
        return True   
    elif str[0].isalnum()is False:
        return isPalindrome(str[1:])
    elif str[-1].isalnum() is False:
        return isPalindrome(str[:-1])
    elif str[0].lower()== str[-1].lower():
        return isPalindrome(str[1:-1])
    else: return False


''''
The function isPalindrom takes as input a string. It checks if the values at 
beginning and the end of the string are alphanumeric. If not it calls itself 
again with the reamining string without the alphanumeric symbols. 

If the string is alphanumeric it checks if the first and last character in the 
string are the same. If they are the same, the function calls itself with the 
same string starting from index 1 and -1 until it reaches the base case of 
having 0 or 1 letters left. This returns true. 
Else it returns false for the words that are not palindrom. 
'''