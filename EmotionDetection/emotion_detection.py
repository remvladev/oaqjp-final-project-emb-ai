import requests
import json
import pprint

def emotion_detector(text_to_analyze):
    '''
    Emotion Detector function
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = input, headers=headers)

    formatted_response = json.loads(response.text)

    anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]

    emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': '<name of the dominant emotion>'
    }

    return emotions