# Mentor AI 

Mentor AI toimii mentorina ja opettajana.  
Se on full-stack demo, jossa frontend + backend + LLM on integroitu.

## Endpoint http://127.0.0.1:5000/

# Kielimalli
- Malli: `jobautomation/OpenEuroLLM-Finnish`
- Pyörii **paikallisesti (localhost)**
- Malli **ei sisälly repositoryyn** lataa itse, jos haluat testata oikeasti:
```bash
ollama pull jobautomation/OpenEuroLLM-Finnish
```