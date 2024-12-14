import yt_dlp
import customtkinter as ctk

def Confirmar():
    video_url = campo_link.get()
    choice = campo_format.get()
    download_video_or_audio(video_url, choice)

def download_video_or_audio(url, download_type="video"):
    rotulo.configure(text="Baixando...")
    try:
        # Configurações para o download
        ydl_opts = {}
        if download_type == "audio":
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        else:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',  # Garante o merge em MP4
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',  # Garante o formato final
                }]
            }

        # Baixar o conteúdo
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído com sucesso!")
        rotulo_concluido.configure(text="Download concluído com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        rotulo_concluido.configure(text="Ocorreu um erro: {e}")

# Exemplo de uso
if __name__ == "__main__":

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    janela = ctk.CTk()
    janela.title("Baixar Videos YT")
    janela.geometry("400x500")

    rotulo_link = ctk.CTkLabel(janela, text="Insira o link:")
    rotulo_link.pack(pady=(20, 5))
    campo_link = ctk.CTkEntry(janela)
    campo_link.pack(pady=5)

    rotulo_format = ctk.CTkLabel(janela, text="Deseja baixar como video ou audio?")
    rotulo_format.pack(pady=(20, 5))
    campo_format = ctk.CTkEntry(janela)
    campo_format.pack(pady=5)

    botao_confirmar = ctk.CTkButton(janela, text="Confirmar", command=Confirmar)
    botao_confirmar.pack(pady=(20, 10))

    rotulo = ctk.CTkLabel(janela, text="")
    rotulo.pack(pady=(10, 5))

    rotulo_concluido = ctk.CTkLabel(janela, text="")
    rotulo_concluido.pack(pady=(10, 5))

    # video_url = input("Digite o URL do vídeo do YouTube: ")
    # choice = input("Deseja baixar como 'video' ou 'audio'? ").strip().lower()
    # download_video_or_audio(video_url, choice)


    janela.mainloop()

