x = input('Enter your name here : ')
print('Nice to mieet you ',x)

print("Let's do some calculations. ")
a = int(input('Input a number : '))
b = int(input('Input other number : '))

def calculate(a,b):
    return a + b

y = calculate(a,b)
print('The sume of the numbers is : ',y)

print("Well done {}".format(x))

y = input('Enter your hobby here : ')
print(f" Good to know that. Go on {x}")
