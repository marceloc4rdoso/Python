#WHILE
nota = int(input('Digite a nota: '))
while nota > 10:
    nota = int(input('Nota inválida!\nInforme uma nota entre 0.00 e 10.00 : '))
print(nota)


""" 
a = 0
while a < 10:
    a += 1
    print(a) 
"""



#FOR in FOR
""" 
insertnumber = int(input('Enter Number: '))

for number in range(insertnumber):
    div = 0
    for x in range(1, number + 1):
        mod = number % x
        if mod == 0:
            div += 1
    if div == 2:
        print('{} é um número primo.'. format(number)) """
    
# FOR

""" 
insertnumber = int(input('Enter Number: '))

div = 0
for x in range(1, insertnumber + 1):
    mod = insertnumber % x
    if mod == 0:
        div += 1
if div == 2:
    print('{} é um número primo.'. format(insertnumber))
else:
    print('O número {} não é primo.'. format(insertnumber))
 """