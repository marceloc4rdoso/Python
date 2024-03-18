lines = []
index =[]
campos = []
payslip_data = {}

for i in range(0, 15):
    payslip_data[f"detail_cod{i}"] = lines[index + campos[f"detail_cod{i}"]["linha"]].strip()[campos[f"detail_cod{i}"]["coluna_inicio"]:campos[f"detail_cod{i}"]["coluna_fim"]]
    payslip_data[f"detail_description{i}"] = lines[index + campos[f"detail_description{i}"]["linha"]].strip()[campos[f"detail_description{i}"]["coluna_inicio"]:campos[f"detail_description{i}"]["coluna_fim"]]
    payslip_data[f"detail_ref{i}"] = lines[index + campos[f"detail_ref{i}"]["linha"]].strip()[campos[f"detail_ref{i}"]["coluna_inicio"]:campos[f"detail_ref{i}"]["coluna_fim"]]
    payslip_data[f"detail_credit{i}"] = lines[index + campos[f"detail_credit{i}"]["linha"]].strip()[campos[f"detail_credit{i}"]["coluna_inicio"]:campos[f"detail_credit{i}"]["coluna_fim"]]
    payslip_data[f"detail_debit{i}"] = lines[index + campos[f"detail_debit{i}"]["linha"]].strip()[campos[f"detail_debit{i}"]["coluna_inicio"]:campos[f"detail_debit{i}"]["coluna_fim"]]

