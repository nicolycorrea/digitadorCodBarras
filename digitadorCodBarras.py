import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode
import pyautogui
import threading
import time

def extrair_codigos_de_barras(caminho_arquivo):
    codigos = []
    imagens = convert_from_path(caminho_arquivo)
    for imagem in imagens:
        codigos_encontrados = decode(imagem)
        for codigo in codigos_encontrados:
            codigos.append(codigo.data.decode("utf-8"))
    return codigos

def digitar_codigos_de_barras(codigos):
    for codigo in codigos:
        pyautogui.write(codigo, interval=0.01)  # Aumenta o intervalo entre cada caractere
    exibir_mensagem("O Código de barras foi digitado com sucesso!")

def selecionar_arquivo_e_simular_digitar():
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
    if caminho_arquivo:
        codigos = extrair_codigos_de_barras(caminho_arquivo)
        if codigos:
            # Inicia uma thread para digitar os códigos de barras enquanto mostra o contador
            threading.Thread(target=exibir_contador_e_digitar, args=(codigos,)).start()
        else:
            exibir_mensagem("[ x ] ERRO: Nenhum código de barras foi encontrado no PDF. [ x ]\n\nPor favor, selecione um pdf que possua um código de barras para leitura.")

def exibir_mensagem(mensagem):
    label_mensagem.config(text=mensagem)

def exibir_contador_e_digitar(codigos):
    contador = 5 # Contador inicial
    while contador >= 0:
        if contador > 0:
            exibir_mensagem("Posicione o cursor do mouse onde deseja colar o código de barras.\nDigitação iniciará em {} segundos...".format(contador))
        else:
            exibir_mensagem("Digitando código de barras...")
        contador -= 1
        time.sleep(1)  # Aguarda 1 segundo
    digitar_codigos_de_barras(codigos)


# Função principal
def main():
    global janela_principal, label_mensagem
    
    # Cria a janela principal
    janela_principal = tk.Tk()
    janela_principal.title("Digitador Automático de Código de Barras")
    janela_principal.geometry("800x300")  # Define o tamanho padrão da janela

    # Cria o cabeçalho
    cabecalho = tk.Label(janela_principal, text="Digitador Automático de Código de Barras", font=("Arial", 15, "bold", "italic"))
    cabecalho.pack(pady=10)
    
    # subtítulo 
    label_titulo = tk.Label(janela_principal, text="Clique no botão e selecione o arquivo (.pdf) desejado", font=("Calibri", 12))
    label_titulo.pack(pady=10)

    # Cria o botão para selecionar o arquivo PDF e digitar os códigos de barras
    botao_selecionar = tk.Button(janela_principal, text="Selecionar Arquivo", font=("Calibri", 12, "bold"), bg="blue", fg="white", command=selecionar_arquivo_e_simular_digitar, width=18, height=1)
    botao_selecionar.pack(pady=10)

    # Cria uma etiqueta para exibir mensagens
    label_mensagem = tk.Label(janela_principal, text="", font=("Calibri", 10))
    label_mensagem.pack()

    # Inicia o loop principal da interface gráfica
    janela_principal.mainloop()

# Verifica se o script está sendo executado diretamente e chama a função principal
if __name__ == "__main__":
    main()

