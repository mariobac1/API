from fastapi import FastAPI

app = FastAPI() #Se crea una variable con esta instancia

@app.get('/')
def home():
    return {'Hello': 'World'}