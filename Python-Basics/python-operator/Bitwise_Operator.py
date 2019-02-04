"""
Created on Feb 4 2019 09:07 AM
@author : S C V S L S RAVI KIRAN
"""

'''
Bitwise Operators - Python
Question : https://practice.geeksforgeeks.org/problems/bitwise-operators-python/1/?track=fork-python
'''
"""
{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        b=int(input())
        c=int(input())
        bitwise(a,b,c)
        testcases-=1
        
if __name__=='__main__':
    main()
}
"""

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def bitwise(a,b, c):
    d = a ^ a
    e = c ^ b
    f = a & b
    g = c | (a ^ a)
    e = ~e
    print(d)
    print(~e)
    print(f)
    print(g)
    print(e)
    

