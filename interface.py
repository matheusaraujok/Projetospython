import yt_dlp
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def escolher_pasta():
    """Abre uma janela de diálogo para o usuário escolher a pasta."""
    pasta = filedialog.askdirectory()
    return pasta

def baixar_audio_youtube():
    """
    Baixa o áudio de um vídeo do YouTube em uma pasta especificada pelo usuário,
    permitindo a escolha da pasta através de um diálogo.
    """
    
    link_video = entry_link.get()  # Obtém o link do vídeo inserido pelo usuário

    if not link_video:
        messagebox.showerror("Erro", "Por favor, insira o link do vídeo.")
        return
    
    pasta_destino = escolher_pasta()

    if not pasta_destino:
        messagebox.showwarning("Aviso", "Nenhuma pasta selecionada. O download foi cancelado.")
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
                base_name, ext = os.path.splitext(os.path.join(pasta_destino, info_dict.get('title') + '.' + info_dict.get('ext')))
                new_name = base_name + '.mp3'

                os.rename(os.path.join(pasta_destino, info_dict.get('title') + '.' + info_dict.get('ext')), new_name)
                
                messagebox.showinfo("Sucesso", f"Áudio baixado e salvo como: {new_name}")
            else:
                messagebox.showinfo("Sucesso", f"Áudio baixado e salvo como: {os.path.join(pasta_destino, info_dict.get('title') + '.' + info_dict.get('ext'))}")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante o download: {e}")

# Configuração da janela principal
root = tk.Tk()
root.title("Baixar Áudio do YouTube")
root.geometry("400x200")

# Rótulo
label_instrucoes = tk.Label(root, text="Insira o link do vídeo do YouTube:")
label_instrucoes.pack(pady=10)

# Campo de entrada do link
entry_link = tk.Entry(root, width=40)
entry_link.pack(pady=5)

# Botão para baixar o áudio
btn_baixar = tk.Button(root, text="Baixar Áudio", command=baixar_audio_youtube)
btn_baixar.pack(pady=20)

# Iniciar a interface gráfica
root.mainloop()
