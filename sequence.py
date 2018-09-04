#Algorithm that generates the first n numbers in the sequence 1,2,3,6,11,20,37,__,__,__,...

#Input an integer and set the variable name to n
#Define the first 2 numbers in the sequence sine they do not follow the pattern (and zero although that is not a part of the sequence but it is a part of the pattern)
#Print the first two numbers of the sequence
#While the number is less than the input - 3 the number is the sum of the 3 last numbers before it (main_num = first_num + second_num + third_num)
#I used n-3 because the the first two numbers, 1 and 2 are already printed
#Print the number for each time the while loop runs


n = int(input("Enter the length of the sequence: "))
first_num = 0
second_num = 1
third_num = 2
num=1

print(1)
print(2)

while num <= n-2:
    if n == 1:
        print(1)
        num+=1
    elif n == 2:
        print(2)
        num+=1
    elif n >= 3:
        main_num = first_num + second_num + third_num 
        first_num = second_num
        second_num = third_num
        third_num = main_num
        num +=1
        print(main_num)

    

    
    

