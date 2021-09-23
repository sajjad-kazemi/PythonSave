while True:
    try:
        num1 = int(input('First number:'))
        operator = input('Enter the operator(+ - * / ^):')
        num2 = int(input('Second number:'))
        if operator == '+':
            print('=', num1+num2)
        elif operator == '-':
            print('=', num1-num2)
        elif operator == '*':
            print('=', num1*num2)
        elif operator == '/':
            print('=', num1/num2)
        elif operator == '^':
            print('=', num1**num2)
        else:
            print('Invalid operator!')
        ending = input('do you want to do again?(y/n)').lower()
        if ending == 'y':
            pass
        elif ending == 'n':
            print('bye:)')
            break

    except(ValueError, TypeError):
        print('please enter a valid number!')
        continue
