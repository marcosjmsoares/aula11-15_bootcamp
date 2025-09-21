from .interface.classes.csv_class import CsvProcessor
#import pandas as pd


caminho_csv = './exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_csv = CsvProcessor(caminho_csv)
arquivo_csv.carregar_csv()
print(arquivo_csv.filtrar_por(filtro,limite))
print(arquivo_csv.sub_filtro('preco','10,50'))
print(arquivo_csv.df)