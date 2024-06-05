from fastapi import FastAPI

app = FastAPI(title="API REST", description="Aplicación de ejemplo para examen Devops de Banco Galicia. Manuel Reichel.", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item():
    return {"message": "Ítem creado exitosamente"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"message": f"Ítem con ID {item_id} leído exitosamente"}

@app.put("/items/{item_id}")
async def update_item(item_id: int):
    return {"message": f"Ítem con ID {item_id} actualizado exitosamente"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Ítem con ID {item_id} eliminado exitosamente"}
