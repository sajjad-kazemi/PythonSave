def even(numbers):
    even_list = []
    for number in range(0,len(numbers)):
        if numbers[number] % 2 == 0:
            even_list.append(numbers[number])
    if even_list == []:
        return 'there is no even number!'
    else:
        return even_list

print(even([1,2,3,4,5,6,7,8]))
print(even([89,12,14,36,15,11]))
print(even([1]))

# single number fibonacci 
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        # recursion 
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(1))
print(fibonacci(9))
print(fibonacci(5))


themainlist =[1,1]
def fib(i):
    num1 = 1
    num2 = 1
    for x in range(i+1):
        num3 = num1 + num2
        themainlist.append(num3)
        num1 = num2
        num2 = num3
    print(themainlist)

myinput = int(input('enter the number: '))
fib(myinput)

numbers = [1,9,1,23,11,15,12,9,86,101,9]
# new_numbers = list(set(numbers))
# print(new_numbers)
def del_same_numbers(n):
    empty_list = []
    for i in n:
        if i not in empty_list:
            empty_list.append(i)
    return str(empty_list)

print('DELETE',del_same_numbers(numbers),type(del_same_numbers(numbers)))




