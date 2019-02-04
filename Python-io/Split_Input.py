"""
Created on Feb 4 2019 08:05 AM
@author : S C V S L S RAVI KIRAN
"""

'''
Split the input - Python
Question : https://practice.geeksforgeeks.org/problems/split-the-input-python/1/?track=fork-python
'''
"""
{

def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        inPutS() #the function that gets things done
        testcases-=1
        
if __name__=='__main__':
    main()
}
"""

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def inPutS():
    a=input() ## input in a single line()
    s,i,f = a.split() ## split the a into three parts: string, integer, and f. 
    print(s+" "+str(int(i)+float(f))) ##type cast i to int, f to float. Add i with f. Typecast the result to string