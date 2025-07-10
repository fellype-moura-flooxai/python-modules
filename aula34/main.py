# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
import fitz  # PyMuPDF
from pathlib import Path
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230210.pdf'
PASTA_NOVA.mkdir(exist_ok=True)

# Extrair imagens
doc = fitz.open(RELATORIO_BACEN)

page = doc[0]

for img_index, img in enumerate(page.get_images(full=True)):
    xref = img[0]
    base_image = doc.extract_image(xref)
    image_bytes = base_image["image"]
    image_ext = base_image["ext"]

    image_filename = PASTA_NOVA / f"page0_img{img_index}.{image_ext}"
    with open(image_filename, "wb") as f:
        f.write(image_bytes)

print("Imagens extraídas com sucesso!")

# Dividir páginas com PyPDF2 
reader = PdfReader(RELATORIO_BACEN) 

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)

print("Páginas salvas em arquivos separados com sucesso!")


files = [
    PASTA_NOVA / 'page1.pdf',
    PASTA_NOVA / 'page0.pdf',

]

merger = PdfMerger()
for file in files:
    merger.append(file)  # type: ignore

merger.write(PASTA_NOVA / 'MERGED.pdf')  # type: ignore
merger.close()