print ("My container is online!\n\nThe first 50 members of the Fibonacci sequence are:")

def Fibonacci(x):
   First_Value=1
   Second_Value=1
   for i in range(x):
       Next_value = First_Value
       First_Value = Second_Value
       Second_Value = Next_value + Second_Value
       print(Next_value)

Fibonacci(50)