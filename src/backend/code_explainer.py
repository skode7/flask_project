from ollama import chat
from ollama import ChatResponse


def prompt_to_llm(prompt: str) -> str:
    response: ChatResponse = chat(
        model="jobautomation/OpenEuroLLM-Finnish",
        messages= [
            {
                "role": "system",
                "content": (
                    f"Toimit koodausmentorina sovelluksessa, jossa käyttäjät esittävät ohjelmointiin liittyviä kysymyksiä. "
                    f"Tavoitteesi on auttaa käyttäjiä oppimaan, ei vain ratkaisemaan ongelmia. "
                    f"Älä anna suoraa ratkaisua tai kirjoita valmista koodia ellei käyttäjä nimenomaisesti pyydä sitä. "
                    f"Sen sijaan tue käyttäjän ajattelua kysymällä tarkentavia kysymyksiä, esittämällä vihjeitä ja avaamalla ongelman taustoja. "
                    f"Selitä tarvittaessa käsitteitä ja ehdota, miten käyttäjä voisi lähestyä ongelmaa. "
                    f"Kannusta käyttäjää tutkimaan ja kokeilemaan ratkaisuja itse, sekä tarjoa tarvittaessa lisätukea ja rohkaisua. Ole aina ystävällinen ja kärsivällinen"
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ])

    return response["message"]["content"]