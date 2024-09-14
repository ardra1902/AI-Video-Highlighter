import os
from pytube import YouTube
import yt_dlp

def download_audio(youtube_url: str, output_path: str = 'audio.wav') -> str:
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path, 
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'quiet': False,
        'verbose': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0',
        },
        'socket_timeout': 60,  # Increase socket timeout to 60 seconds
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    return output_path

