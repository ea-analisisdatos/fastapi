from typing import List, Optional
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Inicializamos una variable donde tendrá todas las características de una API REST
app = FastAPI()

@app.get("/")
def read_root():
     return {"message": "Bienvenido a la API de Cursos"}


# Acá definimos el modelo
class Curso(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    nombre: str
    descripcion: Optional[str] = None
    nivel: str
    duracion: int

# Simulemos una base de datos
cursos_db = []

# CRUD: Read (Lectura) GET ALL: Leeremos todos los cursos que hayan en la db
@app.get("/cursos/", response_model=List[Curso])
def obtener_cursos():
    return cursos_db

# CRUD: Create (escribir) POST: agregaremos un nuevo recurso a nuestra base de datos
@app.post("/cursos/", response_model=Curso)
def crear_curso(curso: Curso):
    cursos_db.append(curso)
    return curso  # Devuelve el curso creado

# CRUD: Read (lectura) GET (individual): Leeremos el curso que coincida con el ID que pidamos 
@app.get("/cursos/{curso_id}", response_model=Curso)
def obtener_curso(curso_id: str):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso

# CRUD: Update (Actualizar/Modificar) PUT: Modificaremos un recurso que coincida con el ID que mandemos 
@app.put("/cursos/{curso_id}", response_model=Curso)
def actualizar_curso(curso_id: str, curso_actualizado: Curso):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    curso_actualizado.id = curso_id
    index = cursos_db.index(curso)  # Buscamos el indice exacto donde está el curso en nuestra lista (BD)
    cursos_db[index] = curso_actualizado
    return curso_actualizado

# CRUD: Delete (borrado/baja) DELETE: Eliminaremos un recurso que coincida con el ID que mandemos 
@app.delete("/cursos/{curso_id}", response_model=Curso)
def eliminar_curso(curso_id: str):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    cursos_db.remove(curso)
    return curso

# Para ejecutar esta app desde una tablet con Android en la terminal bash pegue el sigueinte comando: uvicorn main:app --reload --host 0.0.0.0 --port 8000
# Para usar la misma interface de FastAPI para probar la API REST: (Corre el enlace generado por el VSCode en la nube que termina en "dev" y agrega /docs) Ejemplo: https://turbo-palm-tree-7g7gr7vpvvrcx77p-8000.app.github.dev/docs