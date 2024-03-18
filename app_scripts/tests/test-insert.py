import os

raw_folder = "I:\\IVALIX\\TXT\\mei\\data\\in\\RAW"
output_folder = "I:\\IVALIX\\TXT\\mei\\data\\in\\"
increment_lines = 14

# percorre todos os arquivos na pasta raw_folder
for filename in os.listdir(raw_folder):
    # verifica se o arquivo é um arquivo de texto
    if filename.endswith(".txt"):
        # cria o caminho completo para o arquivo de entrada e saída
        raw_file = os.path.join(raw_folder, filename)
        output_file = os.path.join(output_folder, "MEI-" + filename)
        
        # abre o arquivo de entrada e lê todas as linhas
        with open(raw_file, 'r') as f:
            linhas = f.readlines()
        
        # percorre todas as linhas do arquivo
        for i, linha in enumerate(linhas):
            # verifica se é o início de um novo holerite
            if linha.startswith('1'):
                # contador de linhas com a string inicial 2P
                count_linhas_2P = 0
                count_linhas_2D = 0

                # percorre as próximas linhas até encontrar a linha com a string inicial 2D
                for j in range(i+1, len(linhas)):
                    if linhas[j].startswith('2D'):
                        break

                    # verifica se a linha tem a string inicial 2P
                    if linhas[j].startswith('2P'):
                        count_linhas_2P += 1
                # adiciona linhas com a string inicial 2 até chegar a 5 linhas
                for k in range(count_linhas_2P, increment_lines):
                    linhas.insert(j, '2P\n')
                    count_linhas_2P += 1
                    j += 1

                # percorre as próximas linhas até encontrar a linha com a string inicial 3
                for j in range(i+1, len(linhas)):
                    if linhas[j].startswith('3'):
                        break

                    # verifica se a linha tem a string inicial 2P
                    if linhas[j].startswith('2D'):
                        count_linhas_2D += 1            

                # adiciona linhas com a string inicial 2 até chegar a 5 linhas
                for k in range(count_linhas_2D, increment_lines):
                    linhas.insert(j, '2D\n')
                    count_linhas_2P += 1
                    j += 1      

        # escreve as linhas no arquivo de saída
        with open(output_file, 'w') as f:
            f.writelines(linhas)
