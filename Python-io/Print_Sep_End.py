"""
Created on Feb 4 2019 07:46 AM
@author : S C V S L S RAVI KIRAN
"""

'''
sep and end in Print()
Question : https://practice.geeksforgeeks.org/problems/sep-and-end-in-print/1/?track=fork-python
'''
"""
{
#Initial Template for Python 3
#Position this line where user code will be pasted.
def main():
    string1 = "Geeks"
    string2 = "For"
    print_func(string1, string2)
    print()
if __name__ == "__main__":
    main()
}
"""

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
#Function using 'end' and 'sep' parameters to print desired output
# string1 = "Geeks"
# string2 = "For"
def print_func(string1, string2):
    print (string1,string2,string1, sep = '$', end = '$')
# Use string1 & string2 with sep and end parameter to print desired output