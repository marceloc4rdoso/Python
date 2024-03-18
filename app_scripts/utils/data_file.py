import os
import datetime

# Nome do diretório onde os arquivos estão localizados
dir_name = 'data'

# Obtém a lista de arquivos no diretório especificado
file_list = os.listdir(dir_name)

# Loop através da lista de arquivos
for file_name in file_list:
    # Verifica se o arquivo é um arquivo de texto
    if file_name.endswith('.txt'):
        # Obtem a data e hora de criação do arquivo
        create_time = datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(dir_name, file_name)))
        # Obtem o tamanho do arquivo em bytes
        file_size = os.path.getsize(os.path.join(dir_name, file_name))
        # Exibe o nome do arquivo, data e hora de criação e tamanho
        print(f'Arquivo: {file_name}\nData e hora de criação: {create_time}\nTamanho: {file_size} bytes\n')
