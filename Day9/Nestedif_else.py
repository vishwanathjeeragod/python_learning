#a=52
#if a%2 == 0:
    #print("even")
    #if(a>30):
        #print("number is greater then 30..great!!")
#print("bye")

#height=int(input("what is your height? "))

#if height>3:
    #print("can ride")
    #age=int(input("what is your age? "))
    #if age<18:
        #print("plz pay 250 Rs.")
    #else:
        #print("plz pay 500 rs.")
#else:
    #print("can't ride")
#print("bye")

num = int(input("Enter a number: "))

if num >= 12:
    if num == 12:
        print("The number is zero.")
    else:
        if num % 2 == 0:
            print("The number is positive and even.")
        else:
            print("The number is positive and odd.")
else:
    print("The number is negative.")