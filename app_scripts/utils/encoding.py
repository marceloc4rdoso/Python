# UTF-8

import os

# Função para normalizar o encoding para UTF-8
def normalize_encoding(filepath):
    with open(filepath, 'r', encoding='latin-1') as f:
        text = f.read()
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

# Pasta onde estão os arquivos TXT
folder_path = 'data'

# Loop para percorrer cada arquivo TXT na pasta
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        filepath = os.path.join(folder_path, filename)
        normalize_encoding(filepath)
        print(f'O arquivo {filename} foi normalizado com sucesso para UTF-8!')
