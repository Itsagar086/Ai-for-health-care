import pandas as pd
import os
from datetime import datetime

FILE = "chat_memory.csv"

def save_chat(message, emotion, stress, depression):

    data = {
        "time": datetime.now(),
        "message": message,
        "emotion": emotion,
        "stress": stress,
        "depression_signal": depression
    }

    df = pd.DataFrame([data])

    if not os.path.exists(FILE):
        df.to_csv(FILE, index=False)
    else:
        df.to_csv(FILE, mode="a", header=False, index=False)