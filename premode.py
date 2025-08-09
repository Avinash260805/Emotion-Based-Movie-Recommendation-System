from deepface import DeepFace
import numpy as np

def detect_emotion(img_np_array):

    result = DeepFace.analyze(img_np_array,actions=['emotion'],enforce_detection=True,detector_backend='retinaface')
    if isinstance(result, list):
        result = result[0]
    dominant_emotion = result['dominant_emotion']
    emotion_scores = result['emotion']
    return dominant_emotion,emotion_scores







