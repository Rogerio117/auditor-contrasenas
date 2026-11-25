from fastapi import FastAPI

app = FastAPI(title="Auditor de Contraseñas")


@app.get("/")
def inicio():
    return {"mensaje": "Hola, el ambiente funciona"}