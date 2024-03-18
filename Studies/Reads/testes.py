import sys
import locale
from datetime import datetime

# Define a localização para Português do Brasil
locale.setlocale(locale.LC_ALL, 'ptg_bra') # No Windows!
# Em outro OS provavelmente será:
# locale.setlocale(locale.LC_ALL, 'pt_BR')

date = ''
info = {}
with open('teste.txt', 'r') as f:
    for line in f.readlines():

        line = line.strip('\n ') # Remove quebras de linhas e espaços

        # Tenta converter a linha atual para uma data (no formato esperado!)
        # Se sucesso, abre uma nova "chave" de conteúdo
        try:
            key = datetime.strptime(line, '%d %B %Y- %A')
            date = key
            info[date] = ''

        # Se falhou, o conteúdo pertence à chave atual (se há uma)
        except ValueError:
            if date != '':
                info[date] += line + '\n'


date = input('Digite a data para consulta:')
try:
    date = datetime.strptime(date, '%d %B %Y- %A')
except ValueError:
    print('O valor [{}] não é uma data válida.'.format(date))
    sys.exit(-1)

print(info[date])