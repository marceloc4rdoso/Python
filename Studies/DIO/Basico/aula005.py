#Tuplas - Imutáveis
lista = [1,10,55,17,12]
lista_animal = ['cachorro', 'gato', 'elefante','lobo','arara']


tupla = (1,10,12,14,3)

print(tupla[3])
print(len(tupla))

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista = list(tupla)
print(type(lista))
lista[0] = 99
print(lista)
#listas - Mutaveis
"""  
lista = [1,10,55,17,12]
lista_animal = ['cachorro', 'gato', 'elefante','lobo','arara']


lista_animal[0] = 'macaco'
print(lista_animal)
print(len(lista_animal))

 """
""" 
#Lista ordenada ascendente
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)
#Lista ordenada ascendente
lista.reverse()
lista_animal.reverse()
print(lista)
print(lista_animal)
 """

#print(lista_animal[1])

#print(min(lista_animal))

""" nova_lista = lista_animal * 3
print(nova_lista) """

""" if 'lobo' in lista_animal:
    print('exite gato na lista')
else:
    print('não existe, será incluido')
    lista_animal.append('lobo')
    print(lista_animal)
#lista_animal.pop(0)
lista_animal.remove('elefante')
print(lista_animal) """
