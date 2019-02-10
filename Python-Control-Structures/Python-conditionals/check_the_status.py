"""
Created on Feb 10 2019 08:15 PM
@author : S C V S L S RAVI KIRAN
"""

'''
Check the status - Python
Question : https://practice.geeksforgeeks.org/problems/check-the-status/1
'''
"""
{
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        a = int(input())
        b = int(input())
        flag = input()
        
        if(flag == "True"):
            flag = True
        else:
            flag = False
        
        if(check_status(a, b, flag) is True):
            print ("True")
        else:
            print ("False")
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
}
"""

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to check value and 
# return accordingly
def check_status(a, b, status):
    if(status == True):
        if(a<0 and b<0):
            return True
        else:
            return False
    elif(a>0 and b>0):
        return False
    elif(a>0 or b>0):
        return True
    else:
        return False