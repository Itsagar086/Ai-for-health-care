from transformers import pipeline

# Load emotion detection model
emotion_classifier = pipeline(
    "text-classification",
    model="bhadresh-savani/distilbert-base-uncased-emotion"
)

def detect_emotion(text):
    
    result = emotion_classifier(text)

    return result[0]