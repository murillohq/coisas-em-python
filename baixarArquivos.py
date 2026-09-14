import yt_dlp
import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
ARQUIVOS_BAIXADOS = os.path.join(DIRETORIO_ATUAL, 'downloads')

def baixar_midia(url):
    if not os.path.exists(ARQUIVOS_BAIXADOS):
        os.makedirs(ARQUIVOS_BAIXADOS)
        print(f"📁 Pasta criada em: {ARQUIVOS_BAIXADOS}")

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(ARQUIVOS_BAIXADOS, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': True,
        'nocheckcertificate': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"⏳ Iniciando download de: {url}...")
            ydl.download([url])
            print(f"\n✅ Salvo com sucesso na pasta: {ARQUIVOS_BAIXADOS}")
    except Exception as e:
        print(f"\n❌ Erro ao baixar: {e}")

if __name__ == "__main__":
    link = input("Digite a URL do vídeo (YouTube, Instagram, TikTok, etc): ")
    if link.strip():
        baixar_midia(link)
    else:
        print("URL inválida.")
