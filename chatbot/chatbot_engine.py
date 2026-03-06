from models.emotion_model import detect_emotion
from memory.memory_store import save_chat
from models.stress_model import detect_stress
from models.depression_model import detect_depression


def generate_response(user_text):

    # Run AI models
    emotion = detect_emotion(user_text)
    stress = detect_stress(user_text)
    depression = detect_depression(user_text)

    emotion_label = emotion["label"]
    stress_label = stress["label"]

    # Response logic
    if emotion_label == "sadness":
        response = "I'm really sorry you're feeling this way. Do you want to talk about what’s bothering you?"

    elif emotion_label == "anger":
        response = "It sounds like something frustrating happened. I'm here to listen."

    elif emotion_label == "fear":
        response = "That sounds really stressful. You're not alone in this."

    elif emotion_label == "joy":
        response = "I'm glad you're feeling good today!"

    else:
        response = "I'm here for you. Tell me more about how you're feeling."
        
    save_chat(user_text, emotion_label, stress_label, depression["label"])

    return {
        "emotion": emotion_label,
        "stress": stress_label,
        "depression_signal": depression["label"],
        "response": response
    }