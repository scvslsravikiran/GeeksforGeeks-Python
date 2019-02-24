"""
Created on Feb 4 2019 02:27 PM
@author : S C V S L S RAVI KIRAN
"""

'''
If Conditional Statements - Python
Question : https://practice.geeksforgeeks.org/problems/if-loop-python/1/?track=python-module-2
'''
"""
{
#Initial Template for Python 3
#Position this line where user code will be pasted.
# Driver code    
def main():
    testcase = int(input())
    
    # loop for testcases
    while(testcase > 0):
        string = input().split()
        string1 = string[0]
        string2 = string[1]
        if(string1 == 'True'):
            string1 = True
        else:
            string1 = False
        
        if(string2 == 'True'):
            string2 = True
        else:
            string2 = False
            
        print(friends_in_trouble(string1, string2))
        
        testcase -= 1
    
if __name__ == '__main__':
    main()
}
"""

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to print True and False for required input
def friends_in_trouble(a_angry, b_angry):
    ##Your code here
    if ((a_angry == True) and (b_angry == True) or 
        (a_angry == False) and (b_angry == False)):
            return True
    return False
    