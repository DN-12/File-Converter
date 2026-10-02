from conversores import planilhas,documentos,imagens,outros

#Entrada De dados 
formato_recebido = input("Coloque o Arquivo: ") 
print("Em qual Arquivo voce quer trasformar?")
formato_desejado = int(input(" \n 1 = EXCEL \n 2 = CSV \n 3 = JPG \n 4 = PNG \n 5 = PDF \n " \
"6 = XML \n 7 = JSON \n 8 = TXT \n 9 = DOCX \n Digite o Numero Desejado: "))
reconhecimento_do_formato = formato_recebido.split(".")[-1].lower()

#Processamento de acordo com a escolha do usuario
if reconhecimento_do_formato == "csv":
    if formato_desejado == 1 :
        planilhas.csv_para_xlsx(formato_recebido)
        print("Arquivo convertido com Sucesso")
    elif formato_desejado == 2: 
        print("Erro: Arquivo ja esta em CSV")
    else:
        print("Erro: Arquivo CSV so pode ser convertido para excel")

elif reconhecimento_do_formato == "xlsx":
    if formato_desejado == 1 :
        print("O Arquivo ja esta em Excel")
    elif formato_desejado == 2 :
        planilhas.xlsx_para_csv(formato_recebido)
        print("Arquivo convertido com Sucesso")
    else: 
        print("Erro")

elif reconhecimento_do_formato == "jpg":
    if formato_desejado == 3:
        print('Erro: Imagem ja esta em JPG')
    elif formato_desejado == 4:
        imagens.jpg_para_png(formato_recebido)
        print("Imagem convertida com Sucesso")
    else:
        print("Imagem não pode ser convertida para formato Arquivo")

elif reconhecimento_do_formato == "png":
    if formato_desejado == 3 :
        imagens.png_para_jpg(formato_recebido)
        print("Imagem convertida com Sucesso")
    elif formato_desejado == 4 :
        print("Erro: Imagem ja esta em PNG")
    else:
        print("Imagem não pode ser convertida para um formato Arquivo")

elif reconhecimento_do_formato == "json":
    if formato_desejado == 2 :
        outros.json_para_csv(formato_recebido)
        print("Arquivo convertido com Sucesso")
    elif formato_desejado == 7:
        print("Erro: Arquivo ja esta em Json")
    else:
        print("Erro")

elif reconhecimento_do_formato == "xml":
    if formato_desejado == 2:
        outros.xml_para_csv(formato_recebido)
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