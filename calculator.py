# Greetings, instructions
print('Greetings, this is Calculator. It can add (+), subtract(-), multiply(*) and divide(/).')

# Data input + operands' verification
input1 = input('Enter your first operand: ')
if str.isdigit(input1):
    operand1 = float(input1)
    command = input('Enter your operator: ')
    input2 = input('Enter your second operand: ')
    if str.isdigit(input2):
        operand2 = float(input2)

        # Calculations, response output
        if operand1 == float(input1) and operand2 == float(input2):
            if command == '+':
                print(operand1 + operand2)
            elif command == '-':
                print(operand1 - operand2)
            elif command == '*':
                print(operand1 * operand2)
            elif command == '/':
                if operand2 != 0:
                    if operand1 % operand2 == 0:
                        print(round(operand1 / operand2))
                    else:
                        print(round((operand1 / operand2), 3))
                else:
                    print('Division by zero is NOT allowed!')
            else:
                print('Your operator is invalid or is not feasible for this Calculator')
    else:
        print('Your second operand is invalid. Please enter a number.')
else:
    print('Your first operand is invalid. Please enter a number.')
