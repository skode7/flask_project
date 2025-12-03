from flask import Flask
from flask_cors import CORS
from ollama import ChatResponse
from ollama import chat
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "asdasd"
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")


# Endpoint käyttäjän kysymystä varten

@app.route("/ask/<prompt>", methods=["GET", "POST"])
def ask(prompt: str):
    stream = chat(
        model='gemma3:4b',
        messages=[{'role': 'user', 'content': prompt}],
        stream=True,
    )
    in_thinking = False
    content = ""
    thinking = ""
    for chunk in stream:
        if chunk.message.thinking:
            if not in_thinking:
                in_thinking = True
                print(f"Thinking:\n", end="", flush=True)
            print(chunk.message.thinking, end="", flush=True)
            thinking += chunk.message.thinking

        elif chunk.message.content:
            if in_thinking:
                in_thinking = False
                print("\n\nAnswer:\n", end="", flush=True)
            print(chunk.message.content, end="", flush=True)
            content += chunk.message.content


if __name__ == "__main__":
    socketio.run(app, debug=True, host='127.0.0.1', port=5000, allow_unsafe_werkzeug=True)
