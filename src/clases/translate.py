import requests, os, uuid
from dotenv import load_dotenv
load_dotenv()


class Translate():
    
    def __init__(self, text:str, lang:str) -> str:
        self.__original_text = text
        self.__target_language = lang
        
    def get_traduction(self):
        
        # Load the values from .env
        key = os.environ['KEY']
        endpoint = os.environ['ENDPOINT']
        location = os.environ['LOCATION']
        
        # Indicate that we want to translate and the API version (3.0) and the target language
        path = '/translate?api-version=3.0'
        
        # Add the target language parameter
        target_language_parameter = '&to=' + self.__target_language
        
        # Create the full URL
        constructed_url = endpoint + path + target_language_parameter

        # Set up the header information, which includes our subscription key
        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # Create the body of the request with the text to be translated
        body = [{ 'text': self.__original_text }]
        
        # Make the call using post
        translator_request = requests.post(constructed_url, headers=headers, json=body)
        
        # Retrieve the JSON response
        translator_response = translator_request.json()
        
        # Retrieve the translation
        translated_text = translator_response[0]['translations'][0]['text']
        
        return translated_text
        
        
