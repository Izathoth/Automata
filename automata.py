import os
import requests
import zipfile
import shutil

def baixar_arquivo(url, destino):
    resposta = requests.get(url, stream=True)
    with open(destino, 'wb') as arquivo:
        for chunk in resposta.iter_content(chunk_size=8192):
            arquivo.write(chunk)
    print(f"Arquivo baixado: {destino}")

def extrair_arquivo(zip_path, extrair_para):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extrair_para)
    print(f"Arquivos extraídos para: {extrair_para}")

def criar_pasta(pasta):
    if not os.path.exists(pasta):
        os.makedirs(pasta)

def organizar_arquivos(caminho):
    extensoes = {
        'Imagens': ['jpg', 'jpeg', 'png', 'gif'],
        'Documentos': ['pdf', 'docx', 'txt', 'xlsx'],
        'Vídeos': ['mp4', 'avi', 'mov'],
        'Áudio': ['mp3', 'wav'],
        'Outros': []
    }
    relatorio = []

    for arquivo in os.listdir(caminho):
        if os.path.isfile(os.path.join(caminho, arquivo)):
            ext = arquivo.split('.')[-1].lower()
            pasta_destino = 'Outros'
            for categoria, ext_list in extensoes.items():
                if ext in ext_list:
                    pasta_destino = categoria
                    break
            
            caminho_destino = os.path.join(caminho, pasta_destino)
            criar_pasta(caminho_destino)
            shutil.move(os.path.join(caminho, arquivo), caminho_destino)
            relatorio.append(f"{arquivo} -> {pasta_destino}")

    return relatorio

def gerar_relatorio(relatorio, relatorio_path):
    with open(relatorio_path, 'w') as file:
        file.write("Relatório de Organização de Arquivos:\n\n")
        for linha in relatorio:
            file.write(f"{linha}\n")
    print(f"Relatório gerado: {relatorio_path}")

if __name__ == "__main__":
    url = input("Digite o link do arquivo ZIP para download: ")
    arquivo_zip = 'arquivo.zip'
    pasta_extraida = input("Digite o nome da pasta para extrair os arquivos: ")
    relatorio_path = input("Digite o nome do arquivo de relatório (com extensão .txt): ")

    baixar_arquivo(url, arquivo_zip)
    extrair_arquivo(arquivo_zip, pasta_extraida)
    relatorio = organizar_arquivos(pasta_extraida)
    gerar_relatorio(relatorio, relatorio_path)

    print("Processo concluído com sucesso!")