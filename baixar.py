import yt_dlp
import os
import tkinter as tk
from tkinter import filedialog

def escolher_pasta():
    """Abre uma janela de diálogo para o usuário escolher a pasta."""
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do tkinter
    pasta = filedialog.askdirectory()
    return pasta

def baixar_audio_youtube():
    """
    Baixa o áudio de um vídeo do YouTube em uma pasta especificada pelo usuário,
    permitindo a escolha da pasta através de um diálogo.
    """

    while True:
        try:
            link_video = input("Digite o link do vídeo do YouTube: ")
            break
        except Exception as e:
            print(f"Erro ao processar o link. Verifique se ele é válido.\n{e}")
    
    pasta_destino = escolher_pasta()

    if not pasta_destino:
        print("Nenhuma pasta selecionada. O download foi cancelado.")
        return
    
    try:
        print("Baixando áudio...")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
            'noplaylist': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link_video, download=True)
            
            if info_dict and info_dict.get('ext') != 'mp3':
                
                base_name, ext = os.path.splitext(os.path.join(pasta_destino,info_dict.get('title')+'.'+info_dict.get('ext')))
                
                new_name = base_name+'.mp3'

                os.rename(os.path.join(pasta_destino,info_dict.get('title')+'.'+info_dict.get('ext')), new_name)
                
                print(f"Áudio baixado e salvo como: {new_name}")
            else:
               print(f"Áudio baixado e salvo como: {os.path.join(pasta_destino,info_dict.get('title')+'.'+info_dict.get('ext'))}")


    except Exception as e:
        print(f"Ocorreu um erro durante o download: {e}")

if __name__ == "__main__":
    baixar_audio_youtube()