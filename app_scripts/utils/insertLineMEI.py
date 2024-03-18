import os


#raw_file = ("I:\\IVALIX\\TXT\\mei\\data\\in\\RAW\\")
#os.listdir()
#os.listdir(raw_file)
file_name_in = "ENERGEA 47" + ".txt"
file_name_out = file_name_in + "-out.txt"


raw_file = ("I:\\IVALIX\\TXT\\mei\\data\\in\\RAW\\" + file_name_in)
#files = [f for f in os.listdir() if os.path.isdir(f)]
final_file = ("I:\\IVALIX\\TXT\\mei\\data\\in\\" + file_name_out)
increment_lines = 14


# abre o arquivo e lê todas as linhas
with open(raw_file, 'r', encoding="utf8") as f:
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
        

# escreve as linhas no arquivo atualizado
with open(final_file, 'w', encoding="utf8") as f:
    f.writelines(linhas)


