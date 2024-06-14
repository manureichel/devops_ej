from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI(
    title="API REST App! :D",
    description="Aplicación de ejemplo para examen Devops de Banco Galicia. Manuel Reichel.",
    version="1.0.0"
)

# Simulación de una DB
fake_db: Dict[int, 'Item'] = {}

# Modelos Pydantic para validación
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class UpdateItem(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

@app.get("/items", response_model=Dict[int, Item], summary="Listar todos los ítems", description="Devuelve un diccionario con todos los ítems disponibles en la base de datos simulada.")
async def root():
    return fake_db

@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED, summary="Crear un nuevo ítem", description="Crea un nuevo ítem en la base de datos simulada con los datos proporcionados en el cuerpo de la solicitud.")
async def create_item(item: Item):
    item_id = len(fake_db) + 1
    fake_db[item_id] = item
    return item

@app.get("/items/{item_id}", response_model=Item, summary="Obtener un ítem por ID", description="Devuelve los detalles de un ítem específico basado en su ID. Si el ítem no existe, retorna un error 404.")
async def read_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Ítem no encontrado")
    return fake_db[item_id]

@app.put("/items/{item_id}", response_model=Item, summary="Actualizar un ítem por ID", description="Actualiza los detalles de un ítem específico basado en su ID con los datos proporcionados en el cuerpo de la solicitud. Si el ítem no existe, retorna un error 404.")
async def update_item(item_id: int, item: UpdateItem):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Ítem no encontrado")
    stored_item_data = fake_db[item_id].dict()
    updated_item = item.dict(exclude_unset=True)
    stored_item_data.update(updated_item)
    fake_db[item_id] = Item(**stored_item_data)
    return fake_db[item_id]

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar un ítem por ID", description="Elimina un ítem específico basado en su ID. Si el ítem no existe, retorna un error 404.")
async def delete_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Ítem no encontrado")
    del fake_db[item_id]
    return
