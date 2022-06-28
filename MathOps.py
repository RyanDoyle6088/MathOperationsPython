    ###########################################################
    #  Computer Project #5
    #
    #  Set of functions to compute math values and compare to python math functions
    #    prompt for an integer
    #    input an integer
    #    loop while not end-of-data
    #       call function to count number of digits in integer and round to 10 places
    #       output the number of digits
    #       repeat the loop until the input x is put in
    #       
    #       
    ###########################################################t
''' 
Importing math allows the math functions in python to be used and thus be compared to the functions i created
'''
import math

EPSILON = 1.0e-7

def display_options():
    ''' This function displays the menu of options'''
    MENU = '''\nPlease choose one of the options below:
             A. Display the value of the sum of the first N natural numbers. 
             B. Display the approximate value of e.
             C. Display the approximate value of the hyperbolic sine of X.
             D. Display the approximate value of the hyperbolic cosine of X.
             M. Display the menu of options.
             X. Exit from the program.'''
       
    print(MENU)
    print()     
def sum_natural(N):
    
    '''This function is called when i input the variable sum_natural. I state that for the index in range
    beginning at 1 to the value N(user input)+1, the new total is 0 plus the index result.'''
    if N.isdigit():
        N=int(N)
        
        if N>0:
            return((N*(N+1))/2)
        elif N==0:
            print('\n\tError: N was not a valid natural number ['+str(N)+']')
    else:
        print('\n\tError: N was not a valid natural number ['+N+']')
    return None

def approximate_euler():
    '''This function allows us to compare the value of e in python and the value of e calculated through the 
    euler approximation. I found the value of e using the given equation while the absolute value of the term
    is greater than epsilon, the permitivity constant, the next term from the user input equals one divided by
    the factorial of the index, and each time the code formula runs, the index increases by one until it 
    reaches the restriction of epsilon.'''
   
    next_term=1
    index=1
    total=0

    while abs(next_term)>EPSILON:
          total=total+next_term
          next_term=1/math.factorial(index)
          index=index+1
    total=round(total,10)
    return total
    
def approximate_sinh(X):
    try:
        X_flt=float(X)
        new_term=X_flt
        cosh=0
        n=1
        while new_term >= EPSILON:
                cosh += new_term
                new_term = X_flt**(2*n+1)/math.factorial(2*n+1)
                n+=1
        return round(cosh,10)
    except ValueError:
        return None
           
def approximate_cosh(X):
    '''This function, when called, will take the user input to the power of 2 times the index over the factorial
    of two times the index, then the index will go up by one until it reaches the restriction of epsilon.
    We compare this function value to the python math function of the user input and calculate the difference.'''

    try:
        X_flt=float(X)
        new_term=1
        cosh=0
        n=1
        while new_term >= EPSILON:
                cosh += new_term
                new_term = X_flt**(2*n)/math.factorial(2*n)
                n+=1
        return round(cosh,10)
    except ValueError:
        return None

def main():
    '''We use this main function to now go through all the choices in the menu and prompt the user
    to make a choice and enter an input. Whenever there is an inpup, the main function will in turn run
    whatever corresponding function is in the if statements and will return the value necessary.
    I first show the approximation of my functions with whatever input, then I print the math  module which is 
    python's approximation of the functions with whatever input. Lastly, I print the difference
    between the two values. All of the values are rounded to the decimal place 10 and formatted to be spaced
    properly.'''
    display_options()
    choice=input("\n\tEnter option: ").lower()
    if choice.lower()=='x':
           print('Hope to see you again.')
    while choice.lower()!="x":

        if choice=='m' or choice=='M':
           display_options()

        elif choice=='A' or choice=='a':
           N=input("\nEnter N: ")
           total=sum_natural(N)
           
           if total!=None:
                   print('\n\tThe sum: ',int(total))
    
        elif choice=='B' or choice=='b':
            total=approximate_euler()
            print("\n\tApproximation: {:.10f}".format(total))
            print("\tMath module:   {:.10f}".format(round(math.e,10)))
            difference=abs(total-math.e)
            print("\tdifference:    {:.10f}".format(round(difference,10)))

        elif choice=='C' or choice=='c':
           X=input("\n\tEnter X: ")
           try:    
              X=float(X)
              total=approximate_sinh(X)
              print("\n\tApproximation: {:.10f}".format(total))
              print("\tMath module:   {:.10f}".format(round(math.sinh(X),10)))
              difference=abs(total-math.sinh(X))
              print("\tdifference:    {:.10f}".format(round(difference,10)))
              
           except:
              print('\n\tError: X was not a valid float. ['+X+']')
   
        elif choice=='D' or choice=='d':
           user=(input("\n\tEnter X: "))  
           total=approximate_cosh(user)
           if total==None:
               print('\n\tError: X was not a valid float. ['+user+']')
           else:
               print("\n\tApproximation: {:.10f}".format(total))
               print("\tMath module:   {:.10f}".format(round(math.cosh(user),10)))
               difference=abs(total-math.cosh(user))
               print("\tdifference:    {:.10f}".format(round(difference,10)))
        else:
                   print('\nError:  unrecognized option ['+choice.upper()+']')
                   display_options()
        choice=input("\n\tEnter option: ").lower()
        if choice=='x' or choice=='X':
           print('Hope to see you again.')
if __name__ == "__main__":
    main()
