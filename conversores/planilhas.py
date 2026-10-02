from pathlib import Path
import pandas

def csv_para_xlsx(arquivo):
    dados = pandas.read_csv(arquivo)
    nome = Path(arquivo).stem
    dados.to_excel("{0}.xlsx".format(nome),index=False)
def xlsx_para_csv(arquivo):
    dados = pandas.read_excel(arquivo)
    nome = Path(arquivo).stem
    dados.to_csv("{0}.csv".format(nome),index=False)