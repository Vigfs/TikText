import os
import yaml
import yt_dlp

YAML_DIR = './src/config/settings-ytdlp.yaml'
TEMP_DIR = './src/static/temp'

def media_extractor(url):
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

    with open(YAML_DIR, 'r') as f:
        ydl_opts = yaml.safe_load(f)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return 200
