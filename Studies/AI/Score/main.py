import pandas as pd
#from sklearn import LabelEncoder

def get_data_file():
    path = '/workspaces/Python/AI/Score/data/'
    file_input = 'clientes.csv'
    file_using = path + file_input
    return file_using

def view_data_file():
    table_customers = pd.read_csv(get_data_file())
    print(table_customers)
    #checks
    print(table_customers.info())
    print(table_customers.columns)
    return table_customers

view_data_file()
'''
def _columns_transformers():
    
    codifications = LabelEncoder()
    table = pd.read_csv(get_data_file())
    
    for column in table(view_data_file()):
        if table[column].dtype == "object" and column != "score_credito":
            table[column] = codifications.fit_transform(table[column])
    for column in table(view_data_file()):
        if table[column].dtype == "object" and column != "score_credito":
            print(column)
'''       