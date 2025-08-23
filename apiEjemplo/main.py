from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routers import usuarios
from database import get_connection

app = FastAPI()

#configurar cors y cache
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuarios.router)

#servir archivos estáticos con headers de no-cache
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/", response_class=HTMLResponse)
def root():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Id, Nombre, Email FROM Usuarios")
    rows = cursor.fetchall()
    conn.close()
    usuarios_html = ""
    for row in rows:
        usuarios_html += f"""
        <tr>
            <td>{row[0]}</td>
            <td><input type='text' value='{row[1]}' id='nombre-{row[0]}'></td>
            <td><input type='email' value='{row[2]}' id='email-{row[0]}'></td>
            <td>
                <button onclick='actualizarUsuario({row[0]})'>Actualizar</button>
                <button onclick='eliminarUsuario({row[0]})'>Eliminar</button>
            </td>
        </tr>
        """
    with open("templates/index.html", "r", encoding="utf-8") as f:
        html = f.read()
    html = html.replace("<!-- USUARIOS_TABLE_ROWS -->", usuarios_html)
    return html

#Comando para ejecutar:
# uvicorn main:app --reload

"""
El caché es para: El mensaje 
"304 Not Modified" no es realmente un error 
- es una respuesta HTTP normal que indica que 
el navegador está usando una versión en 
caché del archivo app.js porque no ha cambiado.
 Es completamente normal y no afecta la funcionalidad.
"""