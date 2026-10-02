from pathlib import Path
import pandas

def json_para_csv(arquivo):
    dados = pandas.read_json(arquivo)
    nome = Path(arquivo).stem
    dados.to_csv("{0}.csv".format(nome))
def xml_para_csv(arquivo):
    dados = pandas.read_xml(arquivo)
    nome = Path(arquivo).stem
    dados.to_csv("{0}.csv".format(nome))