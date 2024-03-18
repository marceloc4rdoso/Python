valueproduct = float(0.40)
#print(valueproduct)
""" 
Tabela de lotes:

lote 1 de 000 a 030 unidades
lote 2 de 031 a 050 unidades
lote 3 de 051 a 100 unidades
lote 4 de 101 a 150 unidades

 """
qtd = int(input('QTD: '))
# Valores por lote
lot1 = float(50)
lot2 = float(55)
lot3 = float(60)
lot4 = float(65)

if qtd <=150:
    print('-'*60)
    print('VALORES POR LOTE')
    print('-'*60)
    if qtd <= 30:
        vlrunt = lot1
    if qtd >= 31 and qtd <= 50:
        vlrunt = lot2
    if qtd >= 51 and qtd <= 100:
        vlrunt = lot3
    if qtd >= 101 and qtd <= 150:
        vlrunt = lot4
    print('-'*60)
    print('DESCRIÇÃO    |  QTD  |   VLR.UNT   | VLR.TOTAL')
    print('Holerite     |   1   |    {}     |  {}'.format(vlrunt, vlrunt))
    print('-'*60)
else:
    vlrtotal = qtd * valueproduct
    print('-'*60)
    print('VALORES POR UNIDADES')
    print('-'*60)
    print('DESCRIÇÃO    |  QTD  |   VLR.UNT   | VLR.TOTAL')
    print('Holerite     |   {} |    {}     |  {}'.format(qtd, valueproduct, vlrtotal))
    print('-'*60)

