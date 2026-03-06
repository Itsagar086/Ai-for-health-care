from transformers import pipeline

# Depression detection model
depression_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base"
)

def detect_depression(text):

    result = depression_classifier(text)

    return result[0]