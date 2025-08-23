import pyodbc

server = 'SANTIAGO\\SQLEXPRESS'
database = 'MIBASE'

connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
)

def get_connection():
    return pyodbc.connect(connection_string)

# CREATE
def crear_usuario(nombre, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Usuarios (Nombre, Email) VALUES (?, ?)", (nombre, email))
    conn.commit()
    conn.close()
    print(f"Usuario '{nombre}' creado.")

# READ
def listar_usuarios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Id, Nombre, Email FROM Usuarios")
    for row in cursor.fetchall():
        print(row)
    conn.close()

# UPDATE
def actualizar_usuario(user_id, nuevo_nombre, nuevo_email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Usuarios SET Nombre = ?, Email = ? WHERE Id = ?",
        (nuevo_nombre, nuevo_email, user_id)
    )
    conn.commit()
    conn.close()
    print(f"Usuario {user_id} actualizado.")

# DELETE
def eliminar_usuario(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE Id = ?", (user_id,))
    conn.commit()
    conn.close()
    print(f"Usuario {user_id} eliminado.")


# -----------------
# PRUEBAS
# -----------------
crear_usuario("Juan Pérez", "juan@example.com")
crear_usuario("Ana López", "ana@example.com")

print("\nLista inicial:")
listar_usuarios()

actualizar_usuario(1, "Juan P.", "juanp@example.com")

print("\nLista después de actualizar:")
listar_usuarios()

eliminar_usuario(2)

print("\nLista después de eliminar:")
listar_usuarios()