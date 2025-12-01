from ollama import chat

model = chat(model="poro-34b-chat")
response = model.chat("Selitä tämä Python-koodi suomeksi:\n\nfor i in range(5): print(i)")
print(response)
