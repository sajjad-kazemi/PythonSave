#if...
from math import floor

x = int(floor(float(input('enter your age: '))))
if x<0:
    print("You don't exist!")
elif x == 0:
    print("You've just been born now :) ")
elif 0<x<=10:
    print("You're such a baby :)")
elif 10<x<20:
    print("you're a teenager still a kid :) ")
elif 20<=x<40:
    print("You're adult.")
elif 40<=x<60:
    print("You're getting older and older from now...")
elif 60<=x<100:
    print("I can call you old now :)")
else:
    print("Congratulation you've seen the 100 springs :)")