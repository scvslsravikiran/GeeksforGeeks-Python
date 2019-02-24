"""
Created on Feb 24 2019 06:20 PM
@author : S C V S L S RAVI KIRAN
"""

'''
For Loop 2- Python
Question : https://practice.geeksforgeeks.org/problems/for-loop-2-python/1/?track=python-module-2
'''
"""
{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        mystr=(input())
        stringJumper(mystr)
        print()##separating testcases outputs by newlines
        testcases-=1
        
if __name__=='__main__':
    main()
}
"""
''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def stringJumper(str):
    for i in range(0,len(str),2): ## from 0 to length of str and skip 2
        print(str[i], end="") ##printing character and separating characters by nothing
