list1 = [12,4236,7584,653,1234215,78,0,-10826,1]
i = 0
max = 0 
for i in list1:
    if max<i:
        max=i
    else:
        pass
print('the maxinum number:',max)

list1 = []
while True:
    num1 = int(input('Enter the number: '))
    list1.append(num1)
    if len(list1) > 9:
        Ending = input('finish?(Y/N):')
        if Ending.lower() == 'y':
            break
    else:
        continue
print(list1)

names = ['name1','name2','name3','name4','name5','name6','name7','name8','name9','name10']
filtered_names = []
i = 0
for i in range(0,10):
    if names[i] == 'name5' or names[i] == 'name9':
        continue
    else:
        pass
    filtered_names.append(names[i])
    i += 1
print(filtered_names)

x = 0
while x < 10:
    print(f'the name is ',names[x])
    x += 1

# students_name = ['Sajjad','Sahand','Erfan','Sara','Abolfazl','Maede']
# for i in range(0,len(students_name)):
#     if students_name[i] == 'Erfan':
#         continue
#         # break
#     else:
#         print(students_name[i])
# start_number = int(input("START NUMBER: "))
# finish_number = int(input("FINISH NUMBER: "))
# even_numbers = []
# odd_numbers = []
# for i in range(start_number,finish_number):
#     if i % 2 == 0:
#         even_numbers.append(i)
#     else:
#         odd_numbers.append(i)

# print("Even numbers is: ",even_numbers,'\n',"Odd Numbers is: ",odd_numbers)
# i = 0
# while i < 50:
#     i = i + 1
#     i += 1
# print(i)

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
