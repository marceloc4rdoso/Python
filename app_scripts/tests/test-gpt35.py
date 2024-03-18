import csv
import duplex

input_file = 'data/MAR-2023.txt'
output_file = 'data/output.csv'
marcador = "ANDRES ROMANO"

common_information = marcador
accountant_payslips = 0

payslip_fields = {
    #Head payslip    
    "header_company": {"linha": 0, "coluna_inicio": 0, "coluna_fim": 60},
    "header_local": {"linha": 1, "coluna_inicio": 0, "coluna_fim": 60},
    "header_cnpj": {"linha": 2, "coluna_inicio": 0, "coluna_fim": 20},
    "header_competence": {"linha": 2, "coluna_inicio": 45, "coluna_fim": 70},
    "header_id_employee": {"linha":4, "coluna_inicio": 0, "coluna_fim": 4},
    "header_employee": {"linha": 4, "coluna_inicio": 5, "coluna_fim": 36},
    "header_cbo": {"linha": 4, "coluna_inicio": 37, "coluna_fim": 44},
    "header_department": {"linha": 4, "coluna_inicio": 48, "coluna_fim": 66},
    "header_page": {"linha": 4, "coluna_inicio": 67, "coluna_fim": 70},
    "header_post": {"linha": 5, "coluna_inicio": 0, "coluna_fim": 24},
    "header_admission": {"linha": 5, "coluna_inicio": 34, "coluna_fim": 45},
    "header_doc_employee": {"linha": 5, "coluna_inicio": 55, "coluna_fim": 70},
    #Detais payslip
    "detail_cod1":{"linha": 8, "coluna_inicio": 0, "coluna_fim": 4},
    "detail_description1":{"linha": 8, "coluna_inicio": 6, "coluna_fim": 34},
    "detail_ref1":{"linha": 8, "coluna_inicio": 35, "coluna_fim": 43},
    "detail_credit1":{"linha": 8, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit1":{"linha": 8, "coluna_inicio": 57, "coluna_fim": 67},

    "detail_cod2":{"linha": 9, "coluna_inicio": 0, "coluna_fim": 4},
    "detail_description2":{"linha": 9, "coluna_inicio": 6, "coluna_fim": 34},
    "detail_ref2":{"linha": 9, "coluna_inicio": 35, "coluna_fim": 43},
    "detail_credit2":{"linha": 9, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit2":{"linha": 9, "coluna_inicio": 57, "coluna_fim": 67},

    "detail_cod3":{"linha": 10, "coluna_inicio": 0, "coluna_fim": 4},
    "detail_description3":{"linha": 10, "coluna_inicio": 6, "coluna_fim": 34},
    "detail_ref3":{"linha": 10, "coluna_inicio": 35, "coluna_fim": 43},
    "detail_credit3":{"linha": 10, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit3":{"linha": 10, "coluna_inicio": 57, "coluna_fim": 67},

    "detail_cod4":{"linha": 11, "coluna_inicio": 0, "coluna_fim": 4},
    "detail_description4":{"linha": 11, "coluna_inicio": 6, "coluna_fim": 34},
    "detail_ref4":{"linha": 11, "coluna_inicio": 35, "coluna_fim": 43},
    "detail_credit4":{"linha": 11, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit4":{"linha": 11, "coluna_inicio": 57, "coluna_fim": 67},

    "detail_cod5":{"linha": 12, "coluna_inicio": 0, "coluna_fim": 4},
    "detail_description5":{"linha": 12, "coluna_inicio": 6, "coluna_fim": 34},
    "detail_ref5":{"linha": 12, "coluna_inicio": 35, "coluna_fim": 43},
    "detail_credit5":{"linha": 12, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit5":{"linha": 12, "coluna_inicio": 57, "coluna_fim": 67},

    "detail_cod6":{"linha": 13, "coluna_inicio": 0, "coluna_fim": 4},
    "detail_description6":{"linha": 13, "coluna_inicio": 6, "coluna_fim": 34},
    "detail_ref6":{"linha": 13, "coluna_inicio": 35, "coluna_fim": 43},
    "detail_credit6":{"linha": 13, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit6":{"linha": 13, "coluna_inicio": 57, "coluna_fim": 67},

    "detail_cod7":{"linha": 14, "coluna_inicio": 0, "coluna_fim": 4},
    "detail_description7":{"linha": 14, "coluna_inicio": 6, "coluna_fim": 35},
    "detail_ref7":{"linha": 14, "coluna_inicio": 35, "coluna_fim": 43},
    "detail_credit7":{"linha": 14, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit7":{"linha": 14, "coluna_inicio": 57, "coluna_fim": 67},

    "detail_cod8":{"linha": 15, "coluna_inicio": 0, "coluna_fim": 4},
    "detail_description8":{"linha": 15, "coluna_inicio": 6, "coluna_fim": 34},
    "detail_ref8":{"linha": 15, "coluna_inicio": 35, "coluna_fim": 43},
    "detail_credit8":{"linha": 15, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit8":{"linha": 15, "coluna_inicio": 57, "coluna_fim": 67},

    "detail_cod9":{"linha": 16, "coluna_inicio": 0, "coluna_fim": 4},
    "detail_description9":{"linha": 16, "coluna_inicio": 6, "coluna_fim": 34},
    "detail_ref9":{"linha": 16, "coluna_inicio": 35, "coluna_fim": 43},
    "detail_credit9":{"linha": 16, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit9":{"linha": 16, "coluna_inicio": 57, "coluna_fim": 67},

    "detail_cod10":{"linha": 17, "coluna_inicio": 0, "coluna_fim": 4},
    "detail_description10":{"linha": 17, "coluna_inicio": 6, "coluna_fim": 34},
    "detail_ref10":{"linha": 17, "coluna_inicio": 35, "coluna_fim": 43},
    "detail_credit10":{"linha": 17, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit10":{"linha": 17, "coluna_inicio": 57, "coluna_fim": 67},

    "detail_cod11":{"linha": 18, "coluna_inicio": 0, "coluna_fim": 4},
    "detail_description11":{"linha": 18, "coluna_inicio": 6, "coluna_fim": 34},
    "detail_ref11":{"linha": 18, "coluna_inicio": 35, "coluna_fim": 43},
    "detail_credit11":{"linha": 18, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit11":{"linha": 18, "coluna_inicio": 57, "coluna_fim": 67},

    "detail_cod12":{"linha": 19, "coluna_inicio": 0, "coluna_fim": 4},
    "detail_description12":{"linha": 19, "coluna_inicio": 6, "coluna_fim": 34},
    "detail_ref12":{"linha": 19, "coluna_inicio": 35, "coluna_fim": 43},
    "detail_credit12":{"linha": 19, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit12":{"linha": 19, "coluna_inicio": 57, "coluna_fim": 67},

    "detail_cod13":{"linha": 20, "coluna_inicio": 0, "coluna_fim": 4},
    "detail_description13":{"linha": 20, "coluna_inicio": 6, "coluna_fim": 34},
    "detail_ref13":{"linha": 20, "coluna_inicio": 35, "coluna_fim": 43},
    "detail_credit13":{"linha": 20, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit13":{"linha": 20, "coluna_inicio": 57, "coluna_fim": 67},

    "detail_cod14":{"linha": 21, "coluna_inicio": 0, "coluna_fim": 4},
    "detail_description14":{"linha": 21, "coluna_inicio": 6, "coluna_fim": 34},
    "detail_ref14":{"linha": 21, "coluna_inicio": 35, "coluna_fim": 43},
    "detail_credit14":{"linha": 21, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit14":{"linha": 21, "coluna_inicio": 57, "coluna_fim": 67},
    
    "detail_cod15":{"linha": 22, "coluna_inicio": 0, "coluna_fim": 4},
    "detail_description15":{"linha": 22, "coluna_inicio": 6, "coluna_fim": 34},
    "detail_ref15":{"linha": 22, "coluna_inicio": 35, "coluna_fim": 43},
    "detail_credit15":{"linha": 22, "coluna_inicio": 45, "coluna_fim": 55},
    "detail_debit15":{"linha": 22, "coluna_inicio": 57, "coluna_fim": 67},

    #Bottom payslip
    "bottom_credit":{"linha": 24, "coluna_inicio": 45, "coluna_fim": 54},
    "bottom_debit":{"linha": 24, "coluna_inicio": 57, "coluna_fim": 67},
    "bottom_liquid":{"linha": 26, "coluna_inicio": 57, "coluna_fim": 67},
    "bottom_message":{"linha": 24, "coluna_inicio": 0, "coluna_fim": 35},

    "bottom_base_salary":{"linha": 28, "coluna_inicio": 0, "coluna_fim": 11},
    "bottom_base_inss":{"linha": 28, "coluna_inicio": 13, "coluna_fim": 22},
    "bottom_base_fgts":{"linha": 28, "coluna_inicio": 27, "coluna_fim": 36},
    "bottom_fgts_month":{"linha": 28, "coluna_inicio": 37, "coluna_fim": 46},
    "bottom_base_ir":{"linha": 28, "coluna_inicio": 52, "coluna_fim": 61},
    "bottom_band_ir":{"linha": 28, "coluna_inicio": 62, "coluna_fim": 67},
    "bottom_dependents_ir":{"linha": 28, "coluna_inicio": 70, "coluna_fim": 71}
    
}

with open(input_file, "r") as file:
    lines = file.readlines()
    accountant_payslips = sum(1 for line in lines if marcador in line)

print(f"O arquivo contém {accountant_payslips} holerites.")

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    
    # write header row
    header_row = list(payslip_fields.keys())
    writer.writerow(header_row)

    # iterate over lines to extract payslip data
    for index, line in enumerate(lines):
        if marcador in line:
            # extract payslip data
            payslip_data = {}
            for field, info in payslip_fields.items():
                payslip_data[field] = lines[index + info["linha"]].rstrip()[info["coluna_inicio"]:info["coluna_fim"]]
            
            # write payslip data to CSV
            writer.writerow(list(payslip_data.values()))

duplex.crash()
