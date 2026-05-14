import yt_dlp
import sys

link = sys.argv[1]

ydl_opts = {
    'outtmpl': r'C:\Users\famar\Downloads\%(title)s.%(ext)s',
    'format': 'best',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(link, download=False)
    print("Title:", info.get('title'))
    print("Views:", info.get('view_count'))
    ydl.download([link])