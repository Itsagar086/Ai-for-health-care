from models.depression_model import detect_depression

text = "I feel hopeless and tired of everything"

result = detect_depression(text)

print(result)