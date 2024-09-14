import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY") 

def transcribe_audio(file_path: str) -> dict:
    

    try:
        url = "https://api.deepgram.com/v1/listen"
        headers = {
            "Authorization": f"Token {API_KEY}",
            "Content-Type": "audio/wav"  
        }

        with open(file_path, "rb") as file:
            audio_data = file.read()

        response = requests.post(
            url, 
            headers=headers, 
            data=audio_data, 
            params={
                "punctuate": "true", 
                "utterances": "true",  
                "model": "nova"  
            }
        )

        response.raise_for_status()
        return response.json()

    except Exception as e:
        print(f"An error occurred during transcription: {e}")
        import traceback
        traceback.print_exc()
        return {}