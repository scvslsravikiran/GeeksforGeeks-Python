"""
Created on Feb 24 2019 06:30 PM
@author : S C V S L S RAVI KIRAN
"""

'''
Doge Count - Python
Question : https://practice.geeksforgeeks.org/contest-problem/doge/1/
'''
"""
{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str=input()
        print(doge_count(str))
        testcases-=1
        
if __name__=='__main__':
    main()
}
"""

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''
import re
#User function Template for python3
def doge_count(str):
    count=0
    ##Your code here
    for i in range(0, len(str)-3):
        if str[i] == "d" and str[i+1] == "o" and str[i+3] == "e":
            count = count+1
    return count