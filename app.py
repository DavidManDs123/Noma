from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
import openai

app = Flask(__name__)

# 🔑 כאן תכניס את המפתח API שלך מ-OpenAI
openai.api_key = "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"

@app.route("/voice", methods=["POST"])
def voice():
    # מקבל את הטקסט שאמר המשתמש
    user_input = request.form.get("SpeechResult")

    # יוצר תשובה עם ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    bot_reply = response["choices"][0]["message"]["content"]

    # מחזיר את התשובה לשיחה הקולית
    twiml_response = VoiceResponse()
    twiml_response.say(bot_reply, voice="Polly.Zehava-Neural", language="he-IL")
    return str(twiml_response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
