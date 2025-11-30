import pdfplumber
import ollama
import chromadb
import re


def pdf_to_text():
    with pdfplumber.open("./data/Kysymykset.pdf") as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

        text = re.sub(r"\(cid:\d+\)", "", text)
        text = re.sub(r"\[[^\]]*\]", "", text)

        print(text.split(""))


pdf_to_text()