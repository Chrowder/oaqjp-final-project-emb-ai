import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } } 
    response = requests.post(URL, json = myobj, headers=Headers) 


    formatted_response = json.loads(response.text)
    
    result = dict()
    if response.status_code == 200:
        emotion = formatted_response['emotionPredictions'][0]
        result["anger"] = emotion['emotion']['anger']
        result["disgust"] = emotion['emotion']['disgust']
        result["fear"] = emotion['emotion']['fear']
        result["joy"] = emotion['emotion']['joy']
        result["sadness"] = emotion['emotion']['sadness']

        max = result["anger"]
        dominant_emotion = "anger"
        for key, value in result.items():
            if value > max:
                max = value
                dominant_emotion = key
        result["dominant_emotion"] = dominant_emotion

        return result

    result["anger"] = None
    result["disgust"] = None
    result["fear"] = None
    result["joy"] = None
    result["sadness"] = None
    result["dominant_emotion"] = None
    return  result