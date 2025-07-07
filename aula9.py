# os.listdir para navegar em caminhos
# /Users/pcuser/Desktop/EXEMPLO
# C:\Users\pcuser\Desktop\EXEMPLO
# caminho = r'C:\\Users\\pcuser\\Desktop\\EXEMPLO'
import os

caminho = os.path.join('/Users', 'pcuser', 'Desktop', 'EXEMPLO')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)