
import sqlite3

# 1. Conexión: Crea el archivo físico de la base de datos
conexion = sqlite3.connect('clientes_isp.db')

# 2. El Cursor: La herramienta que ejecuta las órdenes
cursor = conexion.cursor()

# 3. La Estructura: Creamos la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        mes TEXT NOT NULL,
        pagado INTEGER NOT NULL
    )
''')

# 4. Guardar y cerrar
conexion.commit()
conexion.close()

print("¡La base de datos 'clientes_isp.db' ha sido creada con éxito!")
