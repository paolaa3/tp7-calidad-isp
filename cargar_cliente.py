import sqlite3

# Conectamos al archivo que ya creamos (el .db)
conexion = sqlite3.connect('clientes_isp.db')
cursor = conexion.cursor()

print("\n--- CARGAR NUEVO PAGO DE CLIENTE ---")

# Estas líneas piden los datos a través del teclado
nombre = input("Nombre del cliente: ")
mes = input("Mes que está pagando: ")
confirmacion = input("¿El pago fue realizado? (s/n): ")

# Convertimos 's' en 1 y cualquier otra cosa en 0 (Lógica Binaria)
pagado = 1 if confirmacion.lower() == 's' else 0

# La orden SQL para insertar los datos
cursor.execute("INSERT INTO clientes (nombre, mes, pagado) VALUES (?, ?, ?)", 
               (nombre, mes, pagado))

# Guardamos los cambios físicamente en el disco
conexion.commit()
conexion.close()

print(f"\n¡Listo! El registro de {nombre} se guardó correctamente.")
