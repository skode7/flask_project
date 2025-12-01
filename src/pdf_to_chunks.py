import pdfplumber
import ollama
import chromadb
import re
import os.path


# Luetaan PDF tiedosto ja palautetaan se listana jossa kysymys per alkio
def pdf_to_text(file_path: str):
    if os.path.exists(file_path):
        with pdfplumber.open(file_path) as pdf:
            text_content = ""
            for page in pdf.pages:
                text_content += page.extract_text()

            text_content = re.sub(r"\(cid:\d+\)", "", text_content)
            text_content = re.sub(r"\[[^\]]*\]", "", text_content)

            chunks = re.findall(r"\d+\.\s.*?(?=\d+\.|$)", text_content, re.DOTALL)
            chunks = [osa.replace("\n", " ").strip() for osa in chunks]

            return chunks
    else:
        print("Path doesn't exist!")
        return None

path = "./data/Kysymykset.pdf"
chunks = pdf_to_text(path)
def chunks_to_embeddings(text_cbunks: list):

