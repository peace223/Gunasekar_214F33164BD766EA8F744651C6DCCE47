# fatctorial function
def factorial(number):
  if number==0 or number==1:
    return 1
  else :
   return number*factorial(number-1)
result=factorial(5) 
print("the given number's factorial  is ",result)