a = int (input ("escriba un número: "))
b = a%3
c = a%5

if b == 0 :
    if c == 0: 
        print ("FizzBuzz")
    else:
        print ("Fizz")
elif c== 0:
    print ("Buzz")
else:
    print (a)
 