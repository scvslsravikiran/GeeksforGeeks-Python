"""
Created on Feb 4 2019 08:00 AM
@author : S C V S L S RAVI KIRAN
"""

'''
Taking input and typecasting - Python
Question : https://practice.geeksforgeeks.org/problems/taking-input-and-typecasting-python/1/?track=fork-python
'''
"""
{
#Initial Template for Python 3
#Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        inPut() #the function that gets things done
        testcases-=1
        
if __name__=='__main__':
    main()

}
"""

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def inPut():
    #Take input and assign the input to a,b,c,d. Please also typecast as type() will produce wrong answer without it
    a= int(input()) ## a is integer
    b= input() ## b is string
    c= float(input()) ## c is float
    d= bool(input()) ## d is a boolean
    
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))