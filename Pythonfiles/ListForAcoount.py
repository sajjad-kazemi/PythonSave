def checklist(x):
    if x.lower() == 'y':
        return True
    elif x.lower() == 'n':
        return False
    else:
        print('invalid answer!')
        return False

sajjadlist = [] # lists of accounts
mohammadlist = []
zohrelist = []
while True:
    myinput = input('enter the username:')
    myinput2 = input('enter the password:')
    if myinput == 'sajjad' and myinput2 == 'sajjad':
        print('Welcome')
        themainlist = sajjadlist
        break
    elif myinput == 'mohammad45' and myinput2 == 'mohammad45':
        print('Welcome')
        themainlist = mohammadlist
        break
    elif myinput == 'zohre12' and myinput2 == 'zohre12':
        print('Welcome')
        themainlist = zohrelist
        break
    else:
        print('the username or password is incorrect please enter again')

print('Please enter your list elements below:')
i = 1
while True:
    command = input('Type>')
    themainlist.append(command)
    if i%10 != 0 :
        i += 1
        continue
    elif i%10 == 0 :
        x = input('Do you want to end it?(y/n)')
        if checklist(x) == True:
            break
        elif checklist(x) == False:
            i+=1
            continue

print(myinput , ' your list is: ',themainlist)