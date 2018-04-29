
def fizzbuzz(nb):
    for x in range(nb) :
        if x%2==0 and x%3==0:
            print("fizzbuzz")
        elif x%3==0:
            print("buzz")
        elif x%2==0:
            print("fizz")
        else:
            print(x)
        while x<30:
            x+=1
            print("i love banana")



fizzbuzz(45)
