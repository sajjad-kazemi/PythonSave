students_name = ['Sajjad','Sahand','Erfan','Sara','Abolfazl','Maede']
for i in range(0,len(students_name)):
    if students_name[i] == 'Erfan':
        continue
        # break
    else:
        print(students_name[i])
start_number = int(input("START NUMBER: "))
finish_number = int(input("FINISH NUMBER: "))
even_numbers = []
odd_numbers = []
for i in range(start_number,finish_number):
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print("Even numbers is: ",even_numbers,'\n',"Odd Numbers is: ",odd_numbers)
i = 0
while i < 50:
    i = i + 1
    i += 1
print(i)

numbers = []
while True:
    number = int(input("Enter a number: "))
    numbers.append(number)
    result = input("finish the numbers: (Y/N)")
    if result == 'Y':
        break
    else:
        continue

print(numbers)




