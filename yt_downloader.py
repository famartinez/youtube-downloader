import yt_dlp
import sys

link = sys.argv[1]

ydl_opts = {
    'outtmpl': r'C:\Users\famar\Downloads\%(title)s.%(ext)s',
    'format': 'bestaudio/best',

    # exact ffmpeg location
    'ffmpeg_location': r'C:\Users\famar\ffmpeg\ffmpeg-2026-05-13-git-a327bc0561-essentials_build\bin',

    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(link, download=False)
    print("Title:", info.get('title'))
    print("Views:", info.get('view_count'))
    ydl.download([link])