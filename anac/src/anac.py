import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

path = os.getenv('path_file')

df = pd.read_json(path, encoding='utf-8-sig')

colunas = ['Numero_da_Ocorrencia', 'Numero_da_Ficha', 'Classificacao_da_Ocorrência', 'Data_da_Ocorrencia', 'UF', 'Descricao_do_Tipo',
            'Categoria_da_Aeronave', 'Operador', 'Tipo_de_Ocorrencia', 'Fase_da_Operacao', 'Operacao', 'Lesoes_Fatais_Tripulantes',
            'Lesoes_Fatais_Passageiros', 'Lesoes_Fatais_Terceiros', 'Modelo', 'CLS','Nome_do_Fabricante']

df = df[colunas]

df = df.rename(
    columns={
        'Numero_da_Ocorrencia' : 'Num_Oco', 'Numero_da_Ficha' : 'Num_Ficha', 'Classificacao_da_Ocorrência' : 'Class_Oco', 'Data_da_Ocorrencia' : 'Data_Oco',
        'Descricao_do_Tipo' : 'Desc_Tipo', 'Categoria_da_Aeronave' : 'Cat_Aero', 'Operador' : 'Op', 'Tipo_de_Ocorrencia' : 'Tipo_Oco', 
        'Lesoes_Fatais_Tripulantes' : 'Les_Fat_Trip', 'Lesoes_Fatais_Passageiros' : 'Les_Fat_Pass', 'Lesoes_Fatais_Terceiros' : 'Les_Fat_Terc', 
        'Nome_do_Fabricante' : 'Fabricante'
    }
).reset_index(drop=True)

print(df.head())