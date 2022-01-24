#Q1
answerOne = 5//3
print("5 divided by 3 without remainders = " + str(answerOne))

#Q2
print("Hello\nWorld\n")
#added extra new line to provide space for next answer

#Q3
postcode = "BT63 9GH"
print(postcode)

#Q4
print(postcode[:4])

#Q5
fruit = ['apples','bannanas','oranges']
print(fruit)

#Q6
fruit[1] = 'pears'
print(fruit)

#Second set of questions
#Q1 USE WHILE LOOPS!

def looper(arg1, arg2):
    """Print a series of numbers"""
    while arg1 < arg2:
        print(arg1, end=' ')
        arg1 += 1
        print()

looper(0, 10)

def looper2(arg1, arg2):
    """Return a series of numbers"""
    result = []
    while arg1 < arg2:
        result.append(arg1)
        arg1 += 1
        return result

looper3 = looper2(0, 10)
print(looper3)

def ask_ok(prompt, retries=4, reminder='Please try again'):
    while True:
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no', 'nop', 'nope'):
            #return False
            retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response')
    print(reminder)

ask_ok('Do you really want to quit?')

    