import os
import instaloader

def download_instagram_post():
    # Solicita o link do post
    post_url = input("Digite o link do post no Instagram: ")
    
    # Solicita o diretório de salvamento
    save_directory = input("Digite o caminho completo da pasta onde deseja salvar: ")
    
    # Verifica se o diretório existe
    if not os.path.exists(save_directory):
        print("Diretório inválido. Verifique o caminho informado.")
        return

    try:
        # Inicializa o Instaloader
        loader = instaloader.Instaloader()
        
        # Extrai o shortcode do post
        shortcode = post_url.split("/p/")[1].split("/")[0]
        
        # Define o diretório de salvamento
        loader.download_post(instaloader.Post.from_shortcode(loader.context, shortcode), target=save_directory)
        print("Download concluído com sucesso!")
    except Exception as e:
        print(f"Erro ao baixar o post: {e}")

if __name__ == "__main__":
    download_instagram_post()
