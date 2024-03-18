import csv

input_file = 'data/MAR-2023.txt'
output_file = 'data/output.csv'

# Define o marcador que indica o início de cada holerite
marcador = "ANDRES ROMANO"

# Define os campos e suas posições no TXT
campos = {
    #Head payslip
    "header_company": {"linha": 0, "coluna_inicio": 0, "coluna_fim": 60},
    "header_id_employee": {"linha":4, "coluna_inicio": 0, "coluna_fim": 6},
    "header_employee": {"linha": 4, "coluna_inicio": 7, "coluna_fim": 44},
    #Detais payslip
    "detail_description1":{"linha": 8, "coluna_inicio": 7, "coluna_fim": 25},
    "detail_credit1":{"linha": 8, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit1":{"linha": 8, "coluna_inicio": 57, "coluna_fim": 67},
    "detail_description2":{"linha": 9, "coluna_inicio": 7, "coluna_fim": 25},
    "detail_credit2":{"linha": 9, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit2":{"linha": 9, "coluna_inicio": 57, "coluna_fim": 67},
    "detail_description3":{"linha": 10, "coluna_inicio": 7, "coluna_fim": 25},
    "detail_credit3":{"linha": 10, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit3":{"linha": 10, "coluna_inicio": 57, "coluna_fim": 67},
    "detail_description4":{"linha": 11, "coluna_inicio": 7, "coluna_fim": 25},
    "detail_credit4":{"linha": 11, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit4":{"linha": 11, "coluna_inicio": 57, "coluna_fim": 67},
    "detail_description5":{"linha": 12, "coluna_inicio": 7, "coluna_fim": 25},
    "detail_credit5":{"linha": 12, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit5":{"linha": 12, "coluna_inicio": 57, "coluna_fim": 67},
    "detail_description6":{"linha": 13, "coluna_inicio": 7, "coluna_fim": 25},
    "detail_credit6":{"linha": 13, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit6":{"linha": 13, "coluna_inicio": 57, "coluna_fim": 67},
    "detail_description7":{"linha": 14, "coluna_inicio": 7, "coluna_fim": 25},
    "detail_credit7":{"linha": 14, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit7":{"linha": 14, "coluna_inicio": 57, "coluna_fim": 67},
    "detail_description8":{"linha": 15, "coluna_inicio": 7, "coluna_fim": 25},
    "detail_credit8":{"linha": 15, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit8":{"linha": 15, "coluna_inicio": 57, "coluna_fim": 67},
    "detail_description9":{"linha": 16, "coluna_inicio": 7, "coluna_fim": 25},
    "detail_credit9":{"linha": 16, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit9":{"linha": 16, "coluna_inicio": 57, "coluna_fim": 67},
    "detail_description10":{"linha": 17, "coluna_inicio": 7, "coluna_fim": 25},
    "detail_credit10":{"linha": 17, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit10":{"linha": 17, "coluna_inicio": 57, "coluna_fim": 67},
    "detail_description11":{"linha": 18, "coluna_inicio": 7, "coluna_fim": 25},
    "detail_credit11":{"linha": 18, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit11":{"linha": 18, "coluna_inicio": 57, "coluna_fim": 67},
    "detail_description12":{"linha": 19, "coluna_inicio": 7, "coluna_fim": 25},
    "detail_credit12":{"linha": 19, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit12":{"linha": 19, "coluna_inicio": 57, "coluna_fim": 67},
    "detail_description13":{"linha": 20, "coluna_inicio": 7, "coluna_fim": 25},
    "detail_credit13":{"linha": 20, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit13":{"linha": 20, "coluna_inicio": 57, "coluna_fim": 67},
    "detail_description14":{"linha": 21, "coluna_inicio": 7, "coluna_fim": 25},
    "detail_credit14":{"linha": 21, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit14":{"linha": 21, "coluna_inicio": 57, "coluna_fim": 67},
    "detail_description15":{"linha": 22, "coluna_inicio": 7, "coluna_fim": 25},
    "detail_credit15":{"linha": 22, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit15":{"linha": 22, "coluna_inicio": 57, "coluna_fim": 67},
    #Bottom payslip
    "bottom_credit":{"linha": 24, "coluna_inicio": 45, "coluna_fim": 55},
    "bottom_debit":{"linha": 24, "coluna_inicio": 57, "coluna_fim": 67},
    "bottom_liquid":{"linha": 25, "coluna_inicio": 57, "coluna_fim": 67},
}

# Define a função para extrair as informações de cada holerite
def extract_payslip_info(lines, marcador):
    payslip_info = {}
    for campo, posicao in campos.items():
        linha = posicao['linha']
        coluna_inicio = posicao['coluna_inicio']
        coluna_fim = posicao['coluna_fim']
        valor = lines[linha][coluna_inicio:coluna_fim].strip()
        payslip_info[campo] = valor
    return payslip_info

# Define a função para exportar as informações para o CSV
def export_to_csv(output_file, payslip_info):
    with open(output_file, mode='a') as file:
        writer = csv.DictWriter(file, fieldnames=campos.keys(), delimiter=';')
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(payslip_info)

# Abre o arquivo de entrada e lê as linhas
with open(input_file, mode='r') as file:
    lines = file.readlines()

# Percorre as linhas do arquivo e extrai as informações de cada holerite
payslip_info = {}
for line in lines:
    if marcador in line:
        payslip_info = extract_payslip_info(lines, marcador)
    else:
        if payslip_info:
            payslip_info['detail_description1'] = line[7:25].strip()
            payslip_info['detail_credit1'] = line[45:55].strip()
            payslip_info['detail_debit1'] = line[57:67].strip()
            export_to_csv(output_file, payslip_info)
