import yt_dlp

def download_video_or_audio(url, download_type="video"):
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

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
if __name__ == "__main__":
    video_url = input("Digite o URL do vídeo do YouTube: ")
    choice = input("Deseja baixar como 'video' ou 'audio'? ").strip().lower()
    download_video_or_audio(video_url, choice)
