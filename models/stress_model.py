from transformers import pipeline

# Stress detection using sentiment model
stress_classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def detect_stress(text):

    result = stress_classifier(text)

    return result[0]