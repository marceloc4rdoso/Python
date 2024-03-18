'''
Esse script abre o arquivo TXT em modo de leitura e lê cada linha procurando 
pela informação comum em todos os cabeçalhos de holerites. Quando encontra essa informação, 
incrementa o contador de holerites. 
No final, o script imprime a quantidade de holerites encontrados no arquivo.
'''

file_path = r'I:/IVALIX/AA-Holerites/emicol/dados/in/012023.txt'
common_information = "61.685.723/0001-66" # Substituir pela informação que se repete em todos os cabeçalhos de holerites

accountant_payslips = 0

with open(file_path, "r") as file:
    for line in file:
        if common_information in line:
            accountant_payslips += 1

print(f"O arquivo contém {accountant_payslips} holerites.")


