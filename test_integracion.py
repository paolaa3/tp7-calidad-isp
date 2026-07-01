import sqlite3

def test_circuito_registro_cliente():

    conexion = sqlite3.connect(':memory:')
    cursor = conexion.cursor()
    
    cursor.execute('''
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            mes TEXT NOT NULL,
            pagado INTEGER NOT NULL
        )
    ''')
  
    cursor.execute("INSERT INTO clientes (nombre, mes, pagado) VALUES (?, ?, ?)", 
                   ("Juan Perez", "Julio", 1))
    conexion.commit()
    
    cursor.execute("SELECT nombre, mes, pagado FROM clientes WHERE nombre='Juan Perez'")
    resultado = cursor.fetchone()
    
    conexion.close()
    assert resultado is not None
    assert resultado[0] == "Juan Perez"
    assert resultado[1] == "Julio"
    assert resultado[2] == 1
