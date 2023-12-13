import random

OPERATORS = ["+", "-", "*"]

def expGen():
    Min_Operand = 2
    Max_Operand = 10
    leftOpe = random.randint(Min_Operand, Max_Operand)
    rightOpe = random.randint(Min_Operand, Max_Operand)
    Operator = random.choice(OPERATORS)

    expression = str(leftOpe) + " " + Operator + " " + str(rightOpe)
    answer = eval(expression)

    return expression, answer

while True:
    perm = input("Want any expression (y/n)?: ")
    if perm.lower() != 'y':
        break

    expression, answer = expGen()
    print(expression, "=" ,answer)
    



