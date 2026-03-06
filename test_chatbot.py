from chatbot.chatbot_engine import generate_response

text = input("You: ")

result = generate_response(text)

print("\nDetected Emotion:", result["emotion"])
print("Stress Level:", result["stress"])
print("Depression Signal:", result["depression_signal"])

print("\nBot:", result["response"])