#1º Bimestre
nota1 = float(input('1º Bimestre: ')) 
if nota1 > 10 or nota1 < 0:
    print('Informe uma nota entre 0.00 e 10.00')
    nota1 = float(input('1º Bimestre: '))
#2º Bimestre
nota2 = float(input('2º Bimestre: '))
if nota2 > 10 or nota2 < 0:
    print('Informe uma nota entre 0.00 e 10.00')
    nota2 = float(input('2º Bimestre: '))
#3º Bimestre
nota3 = float(input('3º Bimestre: '))
if nota3 > 10 or nota3 < 0:
    print('Informe uma nota entre 0.00 e 10.00')
    nota3 = float(input('3º Bimestre: '))
#4º Bimestre
nota4 = float(input('4º Bimestre: '))
if nota4 > 10 or nota4 < 0:
    print('Informe uma nota entre 0.00 e 10.00')
    nota4 = float(input('4º Bimestre: '))
#Média Final
media = (nota1+nota2+nota3+nota4)/4
print('Media final do ano: {:2f}'.format(media))
#Resultado Final
if media >= 6:
    print('Você foi aprovado')
else:
    print('Você foi reprovado')





""" a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
mod_a = a % 2
mod_b = b % 2
if mod_a == 0 or not mod_b > 0:
    print('Foi digitádo números PARES')
else:
    print('Foi digitado números IMPARES') """

""" mod = a % 2 
if mod == 0:
    print('Número PAR')
else:
    print('Número IMPAR')
 """


""" a = int(input('Primeiro valor: '))
b = int(input('Segundo valo: '))
c = int(input('Segundo valo: '))

if a > b and a > c:
    print('O valor de A que é {} é maior!'.format(a))
elif b > a and b > c:
    print('O valor de B que é {} é maior! '.format(b))
if c > b and c > a:
    print('O valor de C que é {} é maior! '.format(c))      
else:
    print('Tudo igual')
print('***** [Final] *****') """

