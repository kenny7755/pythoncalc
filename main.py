print("Our current options are: divide, subtract, add, and multiply")
NumberOne = int(input('Pick your first number: '))
NumberTwo = int(input('Pick your second number: '))
MathMethod = input('Pick your method of solving: ')
method = MathMethod
if (method == 'division' ):
    st = NumberOne/NumberTwo
    print(st)
elif (method == 'subtract' ):
    st = NumberOne - NumberTwo
    print(st)
elif (method == 'add'):
    st = NumberOne + NumberTwo
    print (st)
elif (method == 'multiply'):
    st = NumberOne * NumberTwo
    print(st)
elif (method == 'other'):
    print('Coming soon!')
