# Write a program that prints the numbers from 1 to 100
# For multiples of 3 print “Fizz” instead of the number
# For the multiples of 5 print “Buzz”
# For numbers which are multiples of both 3 and 5 print “FizzBuzz”.

for i in range(1, 101):
    if i % 3 == 0:
        if i % 5 == 0:
            print("FizzBuzz")
        else: print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else: print(i)
