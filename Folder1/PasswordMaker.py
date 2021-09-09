passdict = {'1':'fi','2':'lo','3':'de','4':'be','5':'wa'
            ,'6':'tu','7':'ga','8':'mo','9':'zi','0':'ra'}
x = 0
while True:
    try:
        myinput = int(input("enter:"))
        if len(str(myinput))< 6:
            print("its too short")
            x+=1
        elif x > 0 and len(str(myinput))>=6:
            print("thats a good password!")
            break
        else:
            break
        
    except(ValueError):
        print("passworrd should be a number")
        x+=1

passw = ''
for i in str(myinput):
    passw = passw + passdict.get(i) 

print("your password is: ", passw , "\nDon't forget to copy your password")