from src.speech_recogntion import speechToText
from src.convert_textToVoice import textToSpeech
from src.utils_microphone import record_audio

text = speechToText()
textToSpeech(text)