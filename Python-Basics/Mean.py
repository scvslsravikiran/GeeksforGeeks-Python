"""
Created on Feb 4 2019 11:47 AM
@author : S C V S L S RAVI KIRAN
"""

'''
Mean of 4 digits when 4th digit and mean of 3 digits are given - Python
'''
"""
{
#Initial Template for Python 3
#Position this line where user code will be pasted.
    
    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        d=int(input()) ##taking d as input
        m=int(input()) ## taking mean of 3 numbers
        print(mean(d,m))
        testcases-=1
        
if __name__=='__main__':
    main()
}
"""

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def mean(d,m):
    new_mean = ((3*m) + d) / 4
    return int(new_mean)
    ##Your code here