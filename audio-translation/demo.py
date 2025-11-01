import openai                   
import os                   
from dotenv import load_dotenv          



load_dotenv()
openAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = openAI_API_KEY




audio_file = open("audio.mp3","rb")
output = openai.Audio.translate('whisper-1', audio_file, response_format="text")
print(output)