a = open('input.txt', 'r')
list = []
for i in a:
    list.append(int(i))
number1 = 0
number2 = 0
for x in list:
    for z in list:
        if x + z == 2020:
            number1 = x
            number2 = z
            break
print(number1, number2)
total =  number1 * number2
print(total)


