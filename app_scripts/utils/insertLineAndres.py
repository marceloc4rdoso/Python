raw_file = ("I:\\IVALIX\\TXT\\andresromano\\dados\\in\\consolidado-slb.txt")
final_file = ("I:\\IVALIX\\TXT\\andresromano\\dados\\in\\input.txt")
increment_lines = 22


# abre o arquivo e lê todas as linhas
with open(raw_file, 'r') as f:
    linhas = f.readlines()

# percorre todas as linhas do arquivo
for i, linha in enumerate(linhas):
    # verifica se é o início de um novo holerite
    if linha.startswith('1'):
        # contador de linhas com a string inicial 2
        count_linhas_2 = 0
        
        # percorre as próximas linhas até encontrar a linha com a string inicial 3
        for j in range(i+1, len(linhas)):
            if linhas[j].startswith('3'):
                break
                
            # verifica se a linha tem a string inicial 2
            if linhas[j].startswith('2'):
                count_linhas_2 += 1
        
        # adiciona linhas com a string inicial 2 até chegar a 5 linhas
        for k in range(count_linhas_2, increment_lines):
            linhas.insert(j, '2\n')
            count_linhas_2 += 1
            j += 1

# escreve as linhas no arquivo atualizado
with open(final_file, 'w') as f:
    f.writelines(linhas)
