import requests
import json

from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class Jarvis:
    def __init__(self):
        self.voice_module = VoiceModule()
        self.speech_recognizer = Watson() # Watson api integration
        self.work_module = Worker()
    def run(self):
        while 1:
            request = self.voice_module.listen() # listen for tasks record them and return .flac
            request = self.speech_recognizer.transcript(request)
            task = self.work_module.match(request)
            self.work_module.execute(task)

class VoiceModule:
    def __init__(self):
        pass


class Worker:
    def __init__(self):
        pass

class Watson:

    def __init__(self, key, url):
        self.auth = IAMAuthenticator(key)
        self.service =SpeechToTextV1(authenticator=self.auth)
        self.service.set_service_url(url)
        self.service.set_default_headers({"Content-Type": "audio/flac"})
    
    def transcript(self, file):
        r = str(self.service.recognize(file))
        r = json.loads(r)
        return r["result"]["results"][0]["alternatives"][0]["transcript"]



        

        
