import yt_dlp
import shutil
import os

def download_video_from_youtube(video_url, output_path='video.mp4'):
    print("Iniciando o download do vídeo...")
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'temp_video.%(ext)s',
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Extraindo informações do vídeo: {video_url}")
        info_dict = ydl.extract_info(video_url, download=True)
        video_file_path = 'temp_video.' + info_dict.get('ext', 'mp4')
        print(f"Arquivo baixado temporariamente como: {video_file_path}")
        if not os.path.isfile(video_file_path):
            raise FileNotFoundError(f'Arquivo de vídeo {video_file_path} não encontrado.')
        shutil.copy(video_file_path, output_path)
        print(f'Arquivo de vídeo copiado para: {output_path}')
        os.remove(video_file_path)
        print(f'Arquivo temporário {video_file_path} removido.')
        print(f'Vídeo salvo em {output_path}')

def download_audio_from_youtube(video_url, output_path='audio.mp3'):
    print("Iniciando o download do áudio...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'temp_audio.%(ext)s',
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        audio_file_path = 'temp_audio.' + info_dict.get('ext', 'webm')
        if not os.path.isfile(audio_file_path):
            raise FileNotFoundError(f'Arquivo de áudio {audio_file_path} não encontrado.')
        shutil.copy(audio_file_path, output_path)
        print(f'Áudio salvo em {output_path}')
        os.remove(audio_file_path)

def main():
    print("****************************")
    print("* Instagram: rafael_cyber1 *")
    print("****************************")
    while True:
        print("\nEscolha uma opção:")
        print("1. Baixar vídeo")
        print("2. Baixar áudio")
        print("3. Sair")

        choice = input("Digite o número da opção desejada: ")

        if choice == '1':
            video_url = input('Digite a URL do vídeo do YouTube: ')
            download_video_from_youtube(video_url)
        elif choice == '2':
            video_url = input('Digite a URL do vídeo do YouTube: ')
            download_audio_from_youtube(video_url)
        elif choice == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
