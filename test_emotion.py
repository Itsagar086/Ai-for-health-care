from models.emotion_model import detect_emotion

text = "I feel very lonely today"

result = detect_emotion(text)

print(result)