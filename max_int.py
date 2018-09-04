#Finding the maximum positive integer input by a user
num_int = int(input("Input a number: ")) #Input an integer
#The input has to be a positive integer for the loop to run
max_int = 0         #Set max_int value to 0 to define the variable
while num_int > 0:      #See whether the integer is positive
    if num_int > max_int:    #Find the maximum positive integer
        max_int = num_int
    num_int = int(input("Input a number: "))      #Input an integer
   
print("The maximum is", max_int)  #print maximum  

