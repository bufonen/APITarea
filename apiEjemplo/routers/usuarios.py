from fastapi import APIRouter
from database import get_connection
from models.usuario import Usuario

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.get("/")
def listar_usuarios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Id, Nombre, Email FROM Usuarios")
    rows = cursor.fetchall()
    conn.close()

    return [{"Id": row[0], "Nombre": row[1], "Email": row[2]} for row in rows]

@router.post("/")
def crear_usuario(usuario: Usuario):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Usuarios (Nombre, Email) VALUES (?, ?)",
        (usuario.Nombre, usuario.Email)
    )
    conn.commit()
    conn.close()
    return {"message": f"Usuario '{usuario.Nombre}' creado ✅"}

@router.put("/{user_id}")
def actualizar_usuario(user_id: int, usuario: Usuario):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Usuarios SET Nombre = ?, Email = ? WHERE Id = ?",
        (usuario.Nombre, usuario.Email, user_id)
    )
    conn.commit()
    conn.close()
    return {"message": f"Usuario {user_id} actualizado ✅"}

@router.delete("/{user_id}")
def eliminar_usuario(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE Id = ?", (user_id,))
    conn.commit()
    conn.close()
    return {"message": f"Usuario {user_id} eliminado ✅"}

@router.get("/{user_id}")
def obtener_usuario(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Id, Nombre, Email FROM Usuarios WHERE Id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"Id": row[0], "Nombre": row[1], "Email": row[2]}
    return {"error": "Usuario no encontrado"}
