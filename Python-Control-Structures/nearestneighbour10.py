"""
Created on Feb 24 2019 06:30 PM
@author : S C V S L S RAVI KIRAN
"""

'''
Nearest Neighbour of 10 - Python
Question : https://practice.geeksforgeeks.org/contest-problem/neighbor-of-10/1/
'''
"""
{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        n=int(input())
        print(isNeighbor(n))
        testcases-=1
        
if __name__=='__main__':
    main()
}
"""
''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def isNeighbor(num):
    ##Your code here
    a = num % 10
    if  (10 - (10-a)) <= 2 or (10 - a) <= 2:
        return True
    else:
        return False
