from PIL import Image
from pathlib import Path
def jpg_para_png(arquivo):
    imagem = Image.open(arquivo)
    nome = Path(arquivo).stem
    imagem.save("{0}.png".format(nome))
def png_para_jpg(arquivo):
    imagem = Image.open(arquivo)
    imagem = imagem.convert("RGB")
    nome = Path(arquivo).stem
    imagem.save("{0}.jpg".format(nome))