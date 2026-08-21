import pandas
from PIL import Image
#Funções de conversão
def conversão_csv_para_xlsx(arquivo):
    dados = pandas.read_csv(arquivo)
    nome = arquivo.split(".")[0]
    dados.to_excel("{0}.xlsx".format(nome))
def conversão_xlsx_para_csv(arquivo):
    dados = pandas.read_excel(arquivo)
    nome = arquivo.split(".")[0]
    dados.to_csv("{0}.csv".format(nome))
def conversao_jpg_para_png(arquivo):
    imagem = Image.open(arquivo)
    nome = arquivo.split(".")[0]
    imagem.save("{0}.png".format(nome))
def conversao_png_para_jpg(arquivo):
    imagem = Image.open(arquivo)
    nome = arquivo.split(".")[0]
    imagem.save("{0}.jpg".format(nome))
def conversao_json_para_csv(arquivo):
    dados = pandas.read_json(arquivo)
    nome = arquivo.split(".")[0]
    dados.to_csv("{0}.csv".format(nome))
def conversao_xml_para_csv(arquivo):
    dados = pandas.read_xml(arquivo)
    nome = arquivo.split(".")[0]
    dados.to_csv("{0}.csv".format(nome))
# def conversão_txt_para_csv(arquivo):
#     dados = pandas.read_csv(arquivo)
#     nome = arquivo.split(".")[0]
#     dados.to_csv("{0}.csv".format(nome))


#Entrada De dados 
formato_recebido = input("Coloque o Arquivo: ") 
print("Em qual Arquivo voce quer trasformar?")
formato_desejado = int(input(" \n 1 = EXCEL \n 2 = CSV \n 3 = JPG \n 4 = PNG \n 5 = PDF \n " \
"6 = XML \n 7 = JSON \n 8 = TXT \n 9 = DOCX \n Digite o Numero Desejado: "))
reconhecimento_do_formato = formato_recebido.split(".")[-1].lower()

#Processamento de acordo com a escolha do usuario
if reconhecimento_do_formato == "csv":
    if formato_desejado == 1 :
        conversão_csv_para_xlsx(formato_recebido)
        print("Arquivo convertido com Sucesso")
    elif formato_desejado == 2: 
        print("Erro: Arquivo ja esta em CSV")
    else:
        print("Erro: Arquivo CSV so pode ser convertido para excel")

elif reconhecimento_do_formato == "xlsx":
    if formato_desejado == 1 :
        print("O Arquivo ja esta em Excel")
    elif formato_desejado == 2 :
        conversão_xlsx_para_csv(formato_recebido)
        print("Arquivo convertido com Sucesso")
    else: 
        print("Erro")

elif reconhecimento_do_formato == "jpg":
    if formato_desejado == 3:
        print('Erro: Imagem ja esta em JPG')
    elif formato_desejado == 4:
        conversao_jpg_para_png(formato_recebido)
        print("Imagem convertida com Sucesso")
    else:
        print("Imagem não pode ser convertida para formato Arquivo")

elif reconhecimento_do_formato == "png":
    if formato_desejado == 3 :
        conversao_png_para_jpg(formato_recebido)
        print("Imagem convertida com Sucesso")
    elif formato_desejado == 4 :
        print("Erro: Imagem ja esta em PNG")
    else:
        print("Imagem não pode ser convertida para um formato Arquivo")

elif reconhecimento_do_formato == "json":
    if formato_desejado == 2 :
        conversao_json_para_csv(formato_recebido)
        print("Arquivo convertido com Sucesso")
    elif formato_desejado == 7:
        print("Erro: Arquivo ja esta em Json")
    else:
        print("Erro")

elif reconhecimento_do_formato == "xml":
    if formato_desejado == 2:
        conversao_xml_para_csv(formato_recebido)
        print("Arquivo convertido com Sucesso")
    elif formato_desejado == 6:
        print("Erro: Arquivo ja esta em Xml")
    else:
        print("Erro")

# elif reconhecimento_do_formato == "txt":
#     if formato_desejado == 2:
#         conversão_txt_para_csv(formato_recebido)
#         print("Arquivo convertido com Sucesso")
#     elif formato_desejado == 8:
#         print("Erro: Arquivo ja esta em TxT")
#     else:
#         print("Erro")

else:
    print(f" Arquivo *{formato_recebido}* Invalido")