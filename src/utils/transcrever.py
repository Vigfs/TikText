import whisper
import time
import os

def transcreverAudio(arquivo):
    try:
        carregar_modelo = whisper.load_model("base")
        transcrever = carregar_modelo.transcribe(arquivo)
        return transcrever
    
    except Exception as e:
        return {"error": str(e)}
    finally:
        try:  # limpa o arquivo temporário
            os.remove(arquivo)
        except:
            pass

AUDIO_DIR = './src/static/temp'
def verificar_arquivo():
    caminho_arquivo = os.path.join(AUDIO_DIR, "audio.opus")
    
    while not os.path.isfile(caminho_arquivo):
        time.sleep(5)

def rodar_script():
    verificar_arquivo()
    arquivo = './src/static/temp/audio.opus'
    resultado = transcreverAudio(arquivo)
    return resultado["text"]
