import pandas as pd

input_file = 'data/output.csv'
#output_file = 'data/duplex_output.csv'
output_file = 'data/duplex_output.csv'

def crash():
    # leitura do arquivo de entrada
    df = pd.read_csv(input_file, sep=';')

    # calcula a quantidade de linhas em cada parte
    half = len(df) // 2

    # cria a primeira metade do cabeçalho
    header_a = ['A' + col for col in df.columns]

    # cria a segunda metade do cabeçalho
    header_b = ['B' + col for col in df.columns]

    # separa o dataframe em duas partes
    df_a = df[:half]
    df_b = df[half:]

    # renomeia as colunas da segunda metade do dataframe
    df_b.columns = header_b

    # concatena as duas partes do dataframe
    result = pd.concat([df_a.reset_index(drop=True), df_b.reset_index(drop=True)], axis=1)

    # adiciona o cabeçalho completo no topo
    result.columns = header_a + header_b

    # grava o resultado em um novo arquivo CSV
    result.to_csv(output_file, sep=';', index=False)