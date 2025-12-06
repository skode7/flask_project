from flask import Flask, jsonify, send_from_directory
from flask_cors import cross_origin
from ollama import chat

app = Flask(__name__, static_folder="../frontend")

@app.route("/")
def index():
    return send_from_directory("../frontend", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("../frontend", path)

# Endpoint käyttäjän kysymystä varten
@app.route("/ask/<prompt>", methods=["GET", "POST"])
@cross_origin()
def ask(prompt: str):
    try:
        response = ask_to_llm(prompt)
        return jsonify({"reply": response})
    except Exception as e:
        return {"error": e}


# Välitetään käyttäjän syöte localhost kielimallille ja palautetaan vastaus
def ask_to_llm(prompt: str) -> str:
    response = chat(
        model='jobautomation/OpenEuroLLM-Finnish',
        messages=[
            {"role": "system", "content":(
                f"Olet Mentor-AI: empaattinen, kannustava ja oppimista tukeva mentori."
                f"Tehtävänäsi on ohjeistaa oikeaan suuntaan ja olla tukena, mutta ei antaa heti oikeita vastauksia."
            )},

            {'role': 'user', 'content': prompt}
        ]
    )
    return response.message.content


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)