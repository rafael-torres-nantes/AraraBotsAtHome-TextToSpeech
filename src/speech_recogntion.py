import os
import whisper

def speechToText(audioName='input_audio.wav', directoryName='audio_folder/'):
    # Obtém uma lista de todos os arquivos no diretório
    audioFile = os.path.join(directoryName, audioName)
   
    # Models
    # tiny - base - small - medium
    model = whisper.load_model("small")
    
    # transcribe audio
    text = whisper.transcribe(model=model,audio=audioFile)
    print(text['text'])

    return text['text']

